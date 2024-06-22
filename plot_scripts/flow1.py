from xml.etree import ElementTree as ET
import sys
import matplotlib.pyplot as plt
import seaborn as sns

# Load XML file
et = ET.parse(sys.argv[1])

bitrates = []
losses = []
delays = []

# Extract data from XML
for flow in et.findall("FlowStats/Flow"):
    for tpl in et.findall("Ipv4FlowClassifier/Flow"):
        if tpl.get('flowId') == flow.get('flowId'):
            break
    if tpl.get('destinationPort') == '654':
        continue
    
    losses.append(int(flow.get('lostPackets')))
    
    rxPackets = int(flow.get('rxPackets'))
    if rxPackets == 0:
        bitrates.append(0)
    else:
        t0 = float(flow.get('timeFirstRxPacket')[:-2])
        t1 = float(flow.get("timeLastRxPacket")[:-2])
        duration = (t1 - t0) * 1e-9
        bitrates.append(8 * int(flow.get("rxBytes")) / duration * 1e-3)
        delays.append(float(flow.get('delaySum')[:-2]) * 1e-9 / rxPackets)

# Set seaborn style
sns.set(style="whitegrid")

# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 10))

# Plot bit rates
sns.histplot(bitrates, bins=40, ax=axs[0], color='skyblue', edgecolor='black')
axs[0].set_xlabel("Flow Bit Rates (kb/s)")
axs[0].set_ylabel("Number of Flows")
axs[0].set_title("Distribution of Flow Bit Rates")

# Plot lost packets
sns.histplot(losses, bins=40, ax=axs[1], color='lightgreen', edgecolor='black')
axs[1].set_xlabel("Number of Lost Packets")
axs[1].set_ylabel("Number of Flows")
axs[1].set_title("Distribution of Lost Packets")

# Plot delays
sns.histplot(delays, bins=10, ax=axs[2], color='salmon', edgecolor='black')
axs[2].set_xlabel("Delay in Seconds")
axs[2].set_ylabel("Number of Flows")
axs[2].set_title("Distribution of Delay")

# Adjust layout
plt.tight_layout()

# Save plot to PDF
plt.savefig("results_seaborn.pdf")

# Show plot
plt.show()

