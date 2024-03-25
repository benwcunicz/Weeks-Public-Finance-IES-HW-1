import pandas as pd
import matplotlib.pyplot as plt 

#import data and filter it
def filter_df():
    df_unfiltered = pd.read_csv("C:\\Users\\willb\\OneDrive\\Desktop\\School\\Year_Two\\Summer_Semester\\Public Finance\\public_finance_data.csv")
    unused_columns = ['LOCATION','MEASURE','AGE','DEFINITION','METHODO','Methodology','Unit Code', 'Unit', 'Flag Codes', 'Flags', 'Reference Period','Definition', 'Reference Period Code','PowerCode','TIME', 'PowerCode Code', 'PowerCode']
    df_filtered = df_unfiltered.drop(columns=unused_columns)
    return df_filtered

#function for plotting graph of gini coefficients
def plot_graph(df):
    df_slo = df.loc[df.index <= 5]
    df_costa_rica = df.loc[df.index > 5]

    years_to_plot = [2016,2017,2018,2019,2020,2021]
    plt.plot(years_to_plot,df_costa_rica['Value'], label='Costa Rica',color='red',marker='o', linestyle='-')
    plt.plot(years_to_plot,df_slo['Value'],label='Slovenia',color='blue',marker='o',linestyle='-')

    plt.title('Gini Coefficient Costa Rica vs. Slovenia 2016-2021')
    plt.xlabel('Year')
    plt.ylabel('Gini Coefficient')
    plt.legend()
    plt.show()

#main function
def main():
    df = filter_df()
    plot_graph(df)

if __name__ == "__main__":
    main()