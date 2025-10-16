import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title('STOCK ANALYSIS DASHBOARD')

# Sidebar
st.sidebar.markdown('## **STOCK ANALYSIS**')

# Navigation
selected_option = st.sidebar.radio(
    label='Navigation',
    options=('HOME', 'STOCK ANALYSIS')
)

if selected_option == 'HOME':
    st.write('Welcome to home page!')

elif selected_option == 'STOCK ANALYSIS':
    # Define analysis options inside this block
    analysis_option = st.sidebar.radio(
        label="Go to",
        options=(
            'Top 10 GREEN Stocks',
            'Top 10 RED Stocks',
            'Market Summary',
            'Volatility Analysis',
            'Cumulative Return Over Time',
            'Sector-wise Performance',
            'Stock Price Correlation',
            'Top 5 Gainers and Losers (Month-wise)'
        )
    )

    # 1) Top 10 Green Stocks
    if analysis_option == 'Top 10 GREEN Stocks':
        # Load CSV
        top_10_green = pd.read_csv(r"D:/stock/stock analysis/top_10_green_stocks.csv")

        st.subheader('TOP 10 GREEN STOCKS')
        st.dataframe(top_10_green)

        # Plotting
        st.subheader('Yearly Returns of Top 10 Green Stocks')
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(
            x='Ticker', 
            y='YearlyReturn_2023_2024', 
            data=top_10_green, 
            ax=ax, 
            color='green',
        )
        ax.set_xlabel('Ticker')
        ax.set_ylabel('Yearly Return')
        st.pyplot(fig)

    # 2) Top 10 Red Stocks
    if analysis_option == 'Top 10 RED Stocks':
        # Load CSV
        top_10_red = pd.read_csv(r"D:/stock/stock analysis/top_10_red_stocks.csv")

        st.subheader('TOP 10 RED STOCKS')
        st.dataframe(top_10_red)

        # Plotting
        st.subheader('Yearly Returns of Top 10 Red Stocks')
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(
            x='Ticker', 
            y='YearlyReturn_2023_2024', 
            data=top_10_red, 
            ax=ax, 
            color='red',
        )
        ax.set_xlabel('Ticker')
        ax.set_ylabel('Yearly Return')
        st.pyplot(fig)


    # 3) Market Summary
    if analysis_option == 'Market Summary':
        market_summary = pd.read_csv('D:/stock/stock analysis/market_summary.csv')
        st.subheader('MARKET SUMMARY')
        st.dataframe(market_summary)
        green_red_data = market_summary[market_summary["Metric"].isin(["Number of Green Stocks", "Number of Red Stocks"])]

        labels = green_red_data["Metric"].values
        values = green_red_data["Value"].values

    # pie chart
        st.subheader("Green vs Red Stocks Distribution")

        fig, ax = plt.subplots(figsize=(6,6))
        ax.pie(
              values,
              labels=labels,
              autopct="%1.1f%%",
              startangle=90,
              colors=["green", "red"],
              explode=(0.05, 0)
        )
        ax.set_title("Green vs Red Stocks")
        st.pyplot(fig)

    # 4) volatility analysis
    if analysis_option == 'Volatility Analysis':
        volatility = pd.read_csv('D:/stock/stock analysis/top10_volatility.csv')
        st.subheader('VOLATILITY ANALYSIS')
        st.dataframe(volatility)
        
    #ploting
        st.subheader('VOLATILITY ANALYSIS')
        fig, ax = plt.subplots(figsize = (14, 8))
        sns.barplot(x = 'Ticker', y = 'Volatility_%', data =volatility, ax = ax, palette= 'husl')
        ax.set_xlabel('Ticker', fontsize=12)
        ax.set_ylabel('Volatility', fontsize=12)
        ax.set_title('Stock Volatility (Yearly)', fontsize=14)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    # 5) cumulative return over time
    if analysis_option == 'Cumulative Return Over Time':
       Cumulative_return = pd.read_csv('D:/stock/stock analysis/Cumulative_return.csv')
       st.subheader('CUMULATIVE RETURN OVER TIME')
       st.dataframe(Cumulative_return)
       
    # ploting 
       st.subheader('CUMULATIVE RETURN OVER TIME')
       fig, ax = plt.subplots(figsize = (12,8))
       sns.lineplot(x = 'Ticker', y = 'CumulativeReturn', data = Cumulative_return, ax=ax, marker = 'o')
       ax.set_xlabel('Ticker',fontsize=12)
       ax.set_ylabel('cumultive_return',fontsize=12)
       ax.set_title('Stock Volatility (Yearly)', fontsize=14)
       st.pyplot(fig)

    # 6) Sector-wise Performance
    if analysis_option == 'Sector-wise Performance':
        sector_performance = pd.read_csv('D:/stock/stock analysis/average_yearly_return.csv')
        st.subheader('SECTOR-WISE PERFORMANCE')
        st.dataframe(sector_performance)
        
    # ploting
        st.subheader('SECTOR-WISE PERFORMANCE')
        fig, ax = plt.subplots(figsize = (12,8))
        sns.barplot(x = 'sector', y = 'YearlyReturn_2023_2024',data = sector_performance, ax=ax, palette= 'magma') 
        ax.set_xlabel('sector',fontsize=15)
        ax.set_ylabel('average yearly return(%)',fontsize=12)
        st.pyplot(fig)

    # 7) Stock Price Correlation
    if analysis_option == 'Stock Price Correlation':
        stock_price_correlation = pd.read_csv('D:/stock/stock analysis/top10_corr_matrix.csv',index_col=0)
        st.subheader('TOP 10 STOCK PRICE CORRELATION')
        st.dataframe(stock_price_correlation)

    # ploting
        st.subheader('Correlation Heatmap')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(stock_price_correlation,
                annot=True,       
                fmt=".2f",        
                cmap='coolwarm',  
                linewidths=0.5,   
                ax=ax)
        plt.title('Stock Price Correlation Heatmap')
        st.pyplot(fig)
        
     # Top 5 Gainers (Month-wise)
    if analysis_option == 'Top 5 Gainers and Losers (Month-wise)':
        
        #read csv file
        top_5_gainers = pd.read_csv('D:/stock/stock analysis/top_gainers_monthly.csv')
        
        #dict to store month wise
        monthly_top_5_gainers = {}
        
        #collect unique month
        unique_months = top_5_gainers['month'].unique()
        
        #user to select a month
        selected_month = st.selectbox('select a month', unique_months)
        
        if selected_month:
            top_5_gainers = top_5_gainers[top_5_gainers['month']== selected_month].head(5).reset_index(drop = True)
            monthly_top_5_gainers[str(selected_month)] = top_5_gainers
        
            #display the data for selected month
            st.subheader(f'TOP 5 GAINERS-{selected_month}')
            st.dataframe(top_5_gainers)
            
             #plotings 
            st.subheader(f'TOP 5 GAINERS-{selected_month}')
            fig, ax = plt.subplots(figsize = (10,8))
            sns.barplot(x = 'Ticker', y = 'MonthlyReturn', hue = 'month', data = top_5_gainers , ax = ax, palette= 'viridis')   
            ax.set_xlabel('Ticker',fontsize=12) 
            ax.set_ylabel('monthly_return',fontsize=12)
            st.pyplot(fig)
            
        
    #Top 5 losers(Month_wise)  
    
        #read csv file
        top_5_losers = pd.read_csv('D:/stock/stock analysis/top_losers_monthly.csv')
        
        #dict to store month wise
        monthly_top_5_losers = {}
        
        #collect month wise
        unique_months = top_5_losers['month'].unique()
        
        if selected_month:
            top_5_losers = top_5_losers[top_5_losers['month']== selected_month].head(5).reset_index(drop = True)
            monthly_top_5_losers[str(selected_month)] = top_5_losers
            
            #display the data for selected month
            st.subheader(f'TOP 5 LOSERS-{selected_month}')
            st.dataframe(top_5_losers)
            
            #plotings 
            st.subheader(f'TOP 5 LOSERS-{selected_month}')
            fig, ax = plt.subplots(figsize = (10,8))
            sns.barplot(x = 'Ticker', y = 'MonthlyReturn', hue = 'month', data = top_5_losers, ax = ax, palette= 'husl')   
            ax.set_xlabel('Ticker',fontsize=12) 
            ax.set_ylabel('monthly_return',fontsize=12)
            st.pyplot(fig)    