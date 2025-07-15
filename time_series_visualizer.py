import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",index_col = "date",parse_dates = True)

# Clean data
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(data=df, x=df.index, y="value", ax=ax, color="red", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
   
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    data = df.copy()
    data["year"] = data.index.year
    data ["month"] = data.index.month_name()
    month_order = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
    data["month"] = pd.Categorical(data["month"], categories=month_order, ordered=True)
    df_bar = data.groupby(["year", "month"])["value"].mean().reset_index()

    # Draw bar plot
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data = df_bar, x="year", y="value",hue = "month",hue_order= month_order, ax=ax)
    ax.set_xlabel("Years")
    ax.set_ylabel("Page Views")
    ax.legend(title = "Month",loc ="upper left")


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box["month"] = pd.Categorical(df_box["month"], categories=month_order, ordered=True)

    # Draw box plots (using Seaborn)
    fig, (ax1,ax2) = plt.subplots(1,2 ,figsize=(16, 5))
    sns.boxplot(data = df_box, x="year", y="value", ax=ax1)
    ax1.set_xlabel("Years")
    ax1.set_ylabel("Page Views")
    ax1.set_title("Year-wise Box Plot (Trend)")

    sns.boxplot(data = df_box, x="month", y="value", ax=ax2)
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
    ax2.set_title("Month-wise Box Plot (Seasonality)")





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
