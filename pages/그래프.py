import streamlit as st

# :blue [Streamlit 그래프]
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

##### :orange [st.area_chart()]
st.area_chart(chart_data)

#### :orange[st.line_chart()]
st.line_chart(chart_data)

#### :orange[st.bar_chart()]
st.bar_chart(chart_data)

#### :orange[st.scatter_chart()]
st.scatter_chart(chart_data)

#### :orange[st.map()]
df = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [37.55, 126.92],
    columns=["lat", "lon"]
)
st.map(df)

###:orange [Matplotlib: st.pyplot()]
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig) # 차트 출력

st.divider() # 구분선

###: orange [Altair: st.altair_chart()]
import altair as alt

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(
        x="a", y="b",
        size="c",
        color="c",
        tooltip=["a", "b", "c"]
    )
)

st.altair_chart(c, use_container_width=True)

### : orange [Plotly: st.plotly_chart()]
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

st.plotly_chart(fig, key="iris", on_select="rerun")
