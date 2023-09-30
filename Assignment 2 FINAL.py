#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd

with open('smokedatwithfips.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Loop through each row in the CSV file
    for row in csv_reader:
        # Each row is a list of values
        # Access individual values by index, e.g., row[0] for the first column
        print(row)


# In[51]:


#create data frame that lists only the state and smoke rate
df = pd.read_csv('smokedatwithfips.csv')
for index, row in df.iterrows():
    
        
    df = df.reset_index()

    df = df[[ 'State', 'smokerate2000']]


# In[52]:


df


# In[53]:


#find top 50 smoke rate in the U.S overall
smokerate2000='smokerate2000'
df_sorted=df.sort_values(by=smokerate2000,ascending=False)
top_50=df_sorted.head(50)

print(top_50)


# In[22]:


import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('smokedatwithfips.csv')
G = nx.Graph()


for index, row in df.iterrows():
    
    state = row['State']
    smokerate = row['smokerate2000']
    
    
    G.add_node(state, smokerate=smokerate)  

smoke_rate_groups = {
    ">0.3": nx.Graph(),
    ">0.2": nx.Graph(),
    ">0.1": nx.Graph(),
    ">0.0": nx.Graph()
}

# Iterate through nodes and assign them to respective smoke rate categories
for node, data in G.nodes(data=True):
    smokerate = data['smokerate']
    if smokerate > 0.3:
        smoke_rate_groups[">0.3"].add_node(node)
    elif smokerate > 0.2:
        smoke_rate_groups[">0.2"].add_node(node)
    elif smokerate > 0.1:
        smoke_rate_groups[">0.1"].add_node(node)
    else:
        smoke_rate_groups[">0.0"].add_node(node)

colors = {
    ">0.3": 'red',
    ">0.2": 'green',
    ">0.1": 'blue',
    ">0.0": 'purple'
}

# Create separate layouts for each smoke rate category
layouts = {category: nx.spring_layout(smoke_rate_groups[category], seed=42) for category in smoke_rate_groups}

# Visualize the graph with grouped nodes and colored nodes
plt.figure(figsize=(12, 8))

for category, layout in layouts.items():
    nodes = smoke_rate_groups[category].nodes()
    node_colors = [colors[category]] * len(nodes)  # Assign the color based on the category
    nx.draw(smoke_rate_groups[category], layout, with_labels=True, node_size=500, node_color=node_colors, font_size=12, font_weight='bold', label=category)
    plt.title("State Network Grouped by Smoke Rate Categories")
    plt.axis('off')  # Turn off axis labels
    plt.legend()


# In[50]:


#Find smoke rates from groups in 0.3, 0.2, and 0.1
#0.3
WV_data = df[df['State'] == 'WV']

average_smoke_rate_WV = WV_data['smokerate2000'].mean()

print(f"The average smoke rate for West Virginia is {average_smoke_rate_WV:.2f}")

#0.2
MD_data = df[df["State"]== 'MD']

average_smoke_rate_MD= MD_data['smokerate2000'].mean()


print(f"The average smoke rate for Maryland is {average_smoke_rate_MD:.2f}")

#0.1
UT_data = df[df['State']== 'UT']

average_smoke_rate_UT= UT_data['smokerate2000'].mean()

print(f"The average smoke rate for Utah is {average_smoke_rate_UT:.2f}")


# In[54]:


# Calculate centrality measures for the graph
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

# Find the nodes with the highest centrality scores
top_degree_nodes = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:3]
top_betweenness_nodes = sorted(betweenness_centrality, key=betweenness_centrality.get, reverse=True)[:3]
top_closeness_nodes = sorted(closeness_centrality, key=closeness_centrality.get, reverse=True)[:3]

# Print the top nodes for each centrality measure
print("Top 3 nodes by Degree Centrality:", top_degree_nodes)
print("Top 3 nodes by Betweenness Centrality:", top_betweenness_nodes)
print("Top 3 nodes by Closeness Centrality:", top_closeness_nodes)


# In[ ]:




