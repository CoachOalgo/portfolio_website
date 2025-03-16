import json
import pandas as pd
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DagData
from .forms import DagDataForm


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = DagDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('visualize', pk=form.instance.pk)
    else:
        form = DagDataForm()

    return render(request, 'line_logic_app/home.html', {'form': form})

# line_logic_app/views.py - Adjust template path
def visualize(request, pk):
    dag_data = DagData.objects.get(pk=pk)
    return render(request, 'dag_vis.html', {'dag_data': dag_data})

@csrf_exempt
def get_graph_data(request, pk):
    dag_data = DagData.objeects.get(pk=pk)
    file_path = dag_data.csv_file.path

    # Read the CSV file
    nodes = set()
    for _, row in df.iterrows():
        nodes.add(row['source'])
        nodes.add(row['target'])
    
    node_list = [{"id": node, "label": node} for node in nodes]

    edges_list = []
    for _, row in df.iterrows():
        edges_list.append({
            "from": row['source'],
            "to": row['target'],
            "label": f"Avg: {rpw['average']}\nStd: {row['standard_deviation']}",
            "title": f"Type: {row['resource_type']}",
            "value": float(row['average'])
        })

    graph_data = {
        "nodes": node_list,
        "edges": edges_list
    }

    return JsonResponse(graph_data)