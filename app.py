import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Setup & Layout ---
st.set_page_config(
    page_title="AI Data Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Interactive Data Dashboard for EDA 📊")
st.markdown("""
Welcome to the AI Data Dashboard! Upload a CSV file to instantly gain insights through interactive data tables, 
statistical summaries, dynamic histograms, scatter plots, and a correlation heatmap.
""")

# --- Helper Functions ---
@st.cache_data
def load_data(file):
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

# --- Upload Zone ---
st.sidebar.header("1. Upload Data")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file here", type=['csv'])

if uploaded_file is not None:
    # --- Data Overview ---
    df = load_data(uploaded_file)
    
    if df is not None:
        st.subheader("Data Overview")
        st.markdown("Here's a quick look at the first few rows of your dataset:")
        st.dataframe(df.head())
        
        st.subheader("Statistical Summary")
        st.markdown("Basic statistical details about the numeric columns in your data:")
        st.dataframe(df.describe())
        
        # Get numeric columns for plotting
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        
        if len(numeric_cols) > 0:
            st.divider()
            
            # --- Interactive Visualizations ---
            st.subheader("Explore the Data")
            
            # Use tabs for a clean UI
            tab1, tab2, tab3 = st.tabs(["Distributions", "Relationships", "Correlations"])
            
            with tab1:
                st.markdown("### Interactive Histogram")
                selected_col_hist = st.selectbox("Select a column to view its distribution:", numeric_cols, key='hist_select')
                
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.histplot(data=df, x=selected_col_hist, kde=True, ax=ax, color='#FF4B4B')
                ax.set_title(f'Distribution of {selected_col_hist}')
                ax.set_xlabel(selected_col_hist)
                ax.set_ylabel('Frequency')
                st.pyplot(fig)
                
            with tab2:
                st.markdown("### Interactive Scatter Plot")
                col1, col2 = st.columns(2)
                
                with col1:
                    x_axis = st.selectbox("Select X-axis:", numeric_cols, key='scatter_x')
                with col2:
                    y_axis = st.selectbox("Select Y-axis:", numeric_cols, key='scatter_y', index=min(1, len(numeric_cols)-1))
                
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax, alpha=0.7, color='#FF4B4B')
                ax.set_title(f'Relationship between {x_axis} and {y_axis}')
                st.pyplot(fig)
                
            with tab3:
                st.markdown("### Correlation Heatmap")
                st.markdown("Explore how numeric features correlate with each other (-1 to 1).")
                
                fig, ax = plt.subplots(figsize=(12, 8))
                corr_matrix = df[numeric_cols].corr()
                sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax, linewidths=.5)
                ax.set_title('Correlation Heatmap')
                st.pyplot(fig)
        else:
            st.warning("No numeric columns found in the dataset for visualizations.")
else:
    st.info("Please upload a CSV file in the sidebar to begin.")
