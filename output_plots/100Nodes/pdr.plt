set terminal pdf
set output "pdrthroughput.pdf"
set title "PDR and Throughput analysis of protocols for 100 Nodes Network"

set mytics 2
set boxwidth 0.5
set xtics format ""
set grid ytics
set style data histogram 
set style fill solid
set xtic rotate out
set style histogram cluster 
plot "pdr.txt" using 2:xtic(1) title "AODV" linecolor "red", "pdr.txt" using 3 title "DSDV" linecolor "blue", "pdr.txt" using 4 title "OLSR" linecolor "green"

