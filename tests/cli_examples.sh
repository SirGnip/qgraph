# Quick examples using the CLI
nums="1\n3\n2\n5\n3\n4\n0\n2\n3"
echo -e $nums | python -m qgraph.qgraph_cli --title "first default"
echo -e $nums | python -m qgraph.qgraph_cli line
echo -e $nums | python -m qgraph.qgraph_cli bar
echo -e $nums | python -m qgraph.qgraph_cli pie
echo -e $nums | python -m qgraph.qgraph_cli histogram
