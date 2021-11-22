import networkx as nx
import matplotlib.pyplot as plt
from pip._internal import network


def print_stats(network, name):
    print(name + ':')

    print(' - 平均経路長: {}'.format(nx.average_shortest_path_length(network)))

    clustering = nx.clustering(network)
    print(' - 平均クラスタリング係数: {}'.format(nx.average_clustering(network)))
    print('\t - 各ノードのクラスタリング係数')
    for key, value in clustering.items():
        print('\t\t[{:>2}] : {}'.format(key, value))

    degrees = network.degree()
    average_deg = sum(degree for _, degree in network.degree()) / network.number_of_nodes()
    max_deg = max(degree for _, degree in degrees)
    print(' - 平均次数: {}'.format(average_deg))
    print(' - 最大次数: {}'.format(max_deg))
    print('\t - 各ノードの次数')
    for degree in degrees:
        print('\t\t[{:>2}] : {}'.format(degree[0], degree[1]))
    print()


def plot_network(network):
    pos = nx.spring_layout(network)
    nx.draw_networkx(network, pos, with_labels=True)
    plt.axis("off")
    plt.show()


def plot_degree(network):
    degree_hist = nx.degree_histogram(network)
    x = range(len(degree_hist))
    plt.bar(x, degree_hist, width=0.5, bottom=None, align='center')
    plt.show()


def main():
    # Graphオブジェクトの作成
    Network1 = nx.Graph()
    Network2 = nx.Graph()

    # nodeデータの追加
    Network1.add_nodes_from(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"])
    Network2.add_nodes_from(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"])

    # edgeデータの追加
    Network1.add_edges_from([
        ("0", "1"),
        ("0", "3"),
        ("0", "5"),
        ("0", "8"),
        ("1", "2"),
        ("1", "3"),
        ("1", "9"),
        ("2", "9"),
        ("2", "13"),
        ("3", "6"),
        ("3", "12"),
        ("4", "11"),
        ("4", "13"),
        ("4", "14"),
        ("6", "7"),
        ("7", "13"),
        ("8", "10"),
        ("9", "11"),
        ("9", "15"),
        ("11", "15")
    ])
    Network2.add_edges_from([
        ("0", "1"),
        ("1", "2"),
        ("2", "3"),
        ("3", "4"),
        ("3", "5"),
        ("3", "6"),
        ("3", "8"),
        ("3", "9"),
        ("3", "10"),
        ("3", "11"),
        ("3", "12"),
        ("3", "13"),
        ("3", "14"),
        ("4", "11"),
        ("4", "12"),
        ("4", "13"),
        ("4", "15"),
        ("6", "7"),
        ("12", "13"),
        ("12", "15"),
    ])

    # data を取得
    print_stats(Network1, 'Network1')
    print_stats(Network2, 'Network2')

    # ネットワークの可視化
    plot_network(Network1)
    plot_network(Network2)

    # 次数分布をプロット
    plot_degree(Network1)
    plot_degree(Network2)


if __name__ == "__main__":
    main()
