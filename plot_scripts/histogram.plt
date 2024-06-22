set terminal pdf
set output "delay.pdf"
set title "Delay and Jitter Delay Analysis of protocols for 50 Nodes Network"


set yrange [0:*]

set mytics 2
set boxwidth 0.5
set xtics format ""
set grid ytics
set style data histogram 
set style fill solid
set xtic rotate out
set style histogram cluster 
plot "final.txt" using 2:xtic(1) title "AODV" linecolor "red", "final.txt" using 3 title "DSDV" linecolor "blue", "final.txt" using 4 title "OLSR" linecolor "green"

