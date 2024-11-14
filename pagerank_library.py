import networkx as nx
import tkinter as tk
from tkinter import ttk, Text
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from PIL import Image, ImageTk

# Tworzenie grafu
G = nx.DiGraph()

node_labels = {
    1: "pornhub.com", 2: "xvideos.com", 3: "youporn.com", 4: "redtube.com", 5: "xnxx.com",
    6: "brazzers.com", 7: "naughtyamerica.com", 8: "playboy.com", 9: "spankbang.com", 10: "adultfriendfinder.com",
    11: "onlyfans.com", 12: "cam4.com", 13: "myfreecams.com", 14: "bongacams.com", 15: "chaturbate.com",
    16: "camsoda.com", 17: "stripchat.com", 18: "livejasmin.com", 19: "hentaivn.com", 20: "rule34.com",
    # Additional nodes with adult-related themes
    21: "extralunchmoney.com", 22: "adultsearch.com", 23: "fetlife.com", 24: "cams.com", 25: "xhamster.com",
    26: "lustery.com", 27: "vrbangers.com", 28: "3dxchat.com", 29: "metart.com", 30: "suicidegirls.com",
    31: "joyourself.com", 32: "bad-dragon.com", 33: "adulttime.com", 34: "realitykings.com", 35: "teamskeet.com",
    36: "mofos.com", 37: "bangbros.com", 38: "girlsway.com", 39: "joymii.com", 40: "erome.com",
    41: "lovense.com", 42: "kink.com", 43: "manyvids.com", 44: "justfor.fans", 45: "darkx.com",
    46: "thotsbay.com", 47: "5kporn.com", 48: "hentai-foundry.com", 49: "motherless.com", 50: "newgrounds.com"
}

# Structured connections (edges) - only outgoing links from Pornhub (node 1), others interconnected
edges = [
    # Outgoing links from Pornhub only
    (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10),
    (1, 11), (1, 12), (1, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (1, 20),
    (2, 21), (2, 22), (3, 23), (3, 24), (4, 25), (5, 26),
    (6, 27), (7, 28), (8, 29), (9, 30), (10, 31), (11, 32),
    (12, 33), (13, 34), (14, 35), (15, 36), (16, 37), (17, 38),
    (18, 39), (19, 40), (20, 41), (21, 42), (22, 43), (23, 44),
    (24, 45), (25, 46), (26, 47), (27, 48), (28, 49), (29, 50),
    (2, 3), (4, 5), (6, 7), (8, 9), (10, 11), (12, 13), (14, 15),
    (16, 17), (18, 19), (20, 21), (22, 23), (24, 25), (26, 27),
    (28, 29), (30, 31), (32, 33), (34, 35), (36, 37), (38, 39),
    (40, 41), (42, 43), (44, 45), (46, 47), (48, 49), (50, 2)
]

G.add_edges_from(edges)
nx.set_node_attributes(G, node_labels, 'name')

# Obliczanie PageRank
page_rank = nx.pagerank(G, alpha=0.85)


# GUI Setup
root = tk.Tk()
root.title("Program do wyszukiwania PageRank")
root.geometry("1000x700")

canvas = None  # Global reference to the graph canvas


# Functions for searching, displaying graphs, etc.
def search_pages(graph, query):
    results = []
    for node, data in graph.nodes(data=True):
        name = data.get('name', '').lower()
        if query.lower() in name:
            incoming_edges = list(graph.in_edges(node))
            incoming_rank_contrib = [(src, page_rank[src]) for src, _ in incoming_edges if src != node]
            total_incoming_rank = sum(rank for _, rank in incoming_rank_contrib)

            path = []
            current_node = node
            while current_node is not None:
                path.append(node_labels.get(current_node, str(current_node)))
                predecessors = list(graph.predecessors(current_node))
                current_node = predecessors[0] if predecessors else None

            path.reverse()

            incoming_contrib_names = [(node_labels.get(src, str(src)), page_rank[src]) for src, _ in incoming_edges if src != node]

            results.append((node, name, page_rank[node], total_incoming_rank, incoming_rank_contrib, incoming_contrib_names, path))

    results.sort(key=lambda x: x[2], reverse=True)
    return results


# Function to clear canvas
def clear_canvas():
    global canvas
    if canvas is not None:
        canvas.get_tk_widget().pack_forget()
        canvas = None


# Function to display the graph path
def display_path_graph(path):
    path_graph = nx.DiGraph()
    for i in range(len(path) - 1):
        path_graph.add_edge(path[i], path[i + 1])

    graph_window = tk.Toplevel(root)
    graph_window.title("Graf dla ścieżki")
    graph_window.geometry("800x600")
    graph_window.attributes('-topmost', True)

    fig, ax = plt.subplots(figsize=(10, 10))

    pos = nx.spring_layout(path_graph)
    page_rank = nx.pagerank(path_graph)

    node_sizes = [page_rank[node] * 5000 for node in path_graph.nodes()]
    node_colors = [page_rank[node] for node in path_graph.nodes()]

    nx.draw_networkx_nodes(path_graph, pos, ax=ax, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.Blues, alpha=0.85)
    nx.draw_networkx_edges(path_graph, pos, ax=ax, arrowstyle='-|>', arrowsize=20, edge_color='gray')
    nx.draw_networkx_labels(path_graph, pos, ax=ax, labels={node: str(node) for node in path_graph.nodes()}, font_size=10)

    sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=plt.Normalize(vmin=min(node_colors), vmax=max(node_colors)))
    sm.set_array([])
    ax.figure.colorbar(sm, ax=ax, label="PageRank Wartości")

    ax.set_title("PageRank Wizualizacja")
    ax.axis("off")

    global canvas
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Search function
def on_search(event=None):
    query = entry.get()
    search_results.delete("1.0", "end")
    results = search_pages(G, query)

    for widget in right_frame.winfo_children():
        widget.destroy()

    if results:
        for node, name, rank, total_rank, contrib, incoming, path in results:
            search_results.insert("end", f"Strona: {name}, Węzeł: {node}, PageRank: {rank:.4f}, \nCałkowity wkład: {total_rank:.4f}\n")
            search_results.insert("end", "Wkład innych stron:\n")
            for src_name, src_rank in incoming:
                search_results.insert("end", f"  - {src_name}, PageRank: {src_rank:.4f}\n")

            path_str = " -> ".join(path)
            search_results.insert("end", f"Ścieżka: {path_str}\n")

            button = ttk.Button(right_frame, text=f"Pokaż graf dla {name}", command=lambda p=path: display_path_graph(p))
            button.pack(pady=5)
    else:
        search_results.insert("end", "Brak wyników.\n")


# Function to display the general graph
def display_general_graph():
    graph_window = tk.Toplevel(root)
    graph_window.title("PageRank Wizualizacja")
    graph_window.geometry("800x600")
    graph_window.attributes('-topmost', True)

    fig, ax = plt.subplots(figsize=(10, 10))

    pos = nx.spring_layout(G)
    node_sizes = [page_rank[node] * 5000 for node in G.nodes()]
    node_colors = [page_rank[node] for node in G.nodes()]

    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.Blues, alpha=0.85)
    nx.draw_networkx_edges(G, pos, ax=ax, arrowstyle='-|>', arrowsize=20)
    nx.draw_networkx_labels(G, pos, ax=ax, labels=node_labels, font_size=10)

    sm = plt.cm.ScalarMappable(cmap=plt.cm.Blues, norm=plt.Normalize(vmin=min(node_colors), vmax=max(node_colors)))
    sm.set_array([])
    ax.figure.colorbar(sm, ax=ax, label="PageRank Wartości")

    ax.set_title("PageRank Wizualizacja")
    ax.axis("off")

    global canvas
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Layout configuration
search_frame = tk.Frame(root)
search_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

entry = ttk.Entry(search_frame, width=50)
entry.grid(row=0, column=0, padx=(0, 10))

search_button = ttk.Button(search_frame, text="Szukaj", command=on_search)
search_button.grid(row=0, column=1)

results_frame = tk.Frame(root)
results_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

search_results = Text(results_frame, width=70, height=35)
search_results.grid(row=0, column=0, pady=10)

right_frame = tk.Frame(results_frame)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

general_graph_button = ttk.Button(root, text="Pokaż ogólny graf", command=display_general_graph)
general_graph_button.grid(row=2, column=0, columnspan=2, pady=10)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)
root.grid_rowconfigure(0, weight=0)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=0)

root.mainloop()
