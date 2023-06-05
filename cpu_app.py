import streamlit as st
import psutil
import plotly.graph_objects as go
import time

def get_cpu_load():
    return psutil.cpu_percent(interval=1)

if __name__ == '__main__':
    # Set up Streamlit app
    st.title("CPU Load Gauge")

    # Create a gauge chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=0,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "CPU Load (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'green'},
            'steps': [
                {'range': [0, 50], 'color': 'lightgreen'},
                {'range': [50, 100], 'color': 'blue'}
            ],
            'threshold': {'line': {'color': 'red', 'width': 4},
                          'thickness': 0.75,
                          'value': 0}
        }
    ))

    # Create a placeholder to hold the chart
    chart_placeholder = st.empty()

    # Continuously update and display CPU load
    while True:
        # Get the current CPU load
        cpu_load = get_cpu_load()

        # Update the gauge chart with the current load value
        fig.data[0].value = cpu_load

        # Render and display the updated gauge chart
        chart_placeholder.plotly_chart(fig, use_container_width=True)

        # Wait for 1 second before updating again
        time.sleep(1)
