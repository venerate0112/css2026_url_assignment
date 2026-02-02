import streamlit as st
import pandas as pd
from PIL import Image
import qrcode
from io import BytesIO
import fitz  # PyMuPDF for PDF rendering

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Ecological Role of Macroplastics",
    layout="wide"
)

# --- SIDEBAR NAVIGATION ---
menu = st.sidebar.radio(
    "Navigation",
    [
        "Researcher Profile",
        "Study Overview",
        "Ethical Clearance",
        "Methods",
        "Results",
        "Discussion",
        "Conclusion",
        "Acknowledgments",
        "References"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📄 Documents")

# --- RESEARCHER PROFILE ---
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Load your local researcher image
        try:
            researcher_img = Image.open("profile_pic.png")
            st.image(researcher_img, caption="Venerate Mdaka", use_column_width=True)
        except:
            st.warning("Researcher image not found. Please make sure 'profile_pic.png' is in the correct folder.")
    
    with col2:
        st.markdown("""
        ### Venerate Mdaka
        **BSc Honours in Environmental Science**  
        University of Mpumalanga
        
        ### Research Focus
        - Freshwater Ecology
        - Plastic Pollution Studies
        - Macroinvertebrate Communities
        - Aquatic Habitat Assessment
        
        ### Current Project
        **Ecological Role of Macroplastics as Habitats for Aquatic Macroinvertebrates**  
        Crocodile River, Mpumalanga, South Africa
        """)
    
    st.markdown("---")
    
    # Contact Information in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### Contact Information
        📧 **Email:** [veneratemdakahlonipho@gmail.com](mailto:veneratemdakahlonipho@gmail.com)
        
        🔗 **LinkedIn:** [Venerate Mdaka](https://www.linkedin.com/in/venerate-mdaka-799703279)
        
        🆔 **ORCID:** [0009-0000-0872-3156](https://orcid.org/0009-0000-0872-3156)
        """)
    
    with col2:
        st.markdown("""
        ### Academic Background
        - **BSc Honours in Environmental Science**  
          University of Mpumalanga (2025)
        
        - **Aquatic Systems Research Group (ASRG)**  
          Research affiliate
        
        - **National Research Foundation (NRF)**  
          Scholarship Recipient
        """)
    
    with col3:
        st.markdown("""
        ### Research Skills
        - Field Sampling Techniques
        - Statistical Analysis
        - Laboratory Analysis
        - Scientific Writing
        """)


    st.divider()



st.sidebar.markdown("---")
st.sidebar.markdown("### 📄 Documents")

# Updated file paths
with open("Report_Presentation.pdf", "rb") as file:
    st.sidebar.download_button(
        label="📊 Download Report Presentation (PDF)",
        data=file,
        file_name="Report_Presentation.pdf",
        mime="application/pdf"
    )

with open("Research_study.pdf", "rb") as file:
    st.sidebar.download_button(
        label="📘 Download Research Study (PDF)",
        data=file,
        file_name="Research_study.pdf",
        mime="application/pdf"
    )


# --- STUDY OVERVIEW ---
if menu == "Study Overview":
    st.subheader("Study Overview")
    st.markdown("""
    This study investigated the colonisation of macroplastic debris by aquatic
    macroinvertebrates in the Crocodile River, Mpumalanga, across contrasting seasons.
    """)
    # AIM
    st.markdown("### AIM")
    st.markdown("""
    The study aimed to assess the ecological role of macroplastics as habitats for aquatic macroinvertebrates 
    in the Crocodile River, Mpumalanga.
    """)
    st.markdown("### Objectives")
    st.markdown("""
    - Assess the presence of macroinvertebrate communities on macroplastic debris  
    - Compare diversity between macroplastics and natural substrates  
    - Evaluate seasonal variation in community composition  
    """)
    st.markdown("### Hypotheses")
    st.markdown("""
    - Macroinvertebrate communities will be present on macroplastic debris across seasons.  
    - Macroinvertebrate diversity will differ significantly between macroplastics and natural substrates.  
    """)

# --- ETHICAL CLEARANCE ---
elif menu == "Ethical Clearance":
    st.subheader("Ethical Clearance")
    st.markdown("Ethical approval was obtained prior to field sampling and laboratory analysis.")

    # Render PDF as image using PyMuPDF
    try:
        pdf_path = "Ethical_clearance.pdf"
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)  # first page
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        st.image(img, caption="Ethical Clearance Approval", use_container_width=True)
    except Exception as e:
        st.error(f"Failed to render Ethical Clearance PDF. Error: {e}")

# --- METHODS ---
elif menu == "Methods":
    st.subheader("Methods")

    # Study Area
    st.markdown("### Study Area")
    st.image("Study_Area_Map.png", use_container_width=True)

    st.markdown("""
    Sampling was conducted along the Crocodile River during S1 (cool-dry) and
    S2 (wet-cool) seasons.
    """)

   

    # Environmental Variables
    st.markdown("### Environmental Variables")
    st.markdown("""
    A multiparameter probe measured temperature, pH, conductivity,
    dissolved oxygen (DO), oxidation-reduction potential (ORP),
    and total dissolved solids.
    """)

    # Macroinvertebrate Sampling
    st.markdown("### Macroinvertebrate Sampling")
    st.markdown("""
    A random 20-minute timed sampling protocol was used to dislodge
    macroinvertebrates into a net. Samples were preserved in 70% ethanol,
    identified under a microscope, and counted.
    """)

    # Field Sampling (moved here after Macroinvertebrate Sampling)
    st.markdown("### Field Sampling")
    st.markdown("""
    Sampling was conducted across two distinct seasonal periods:  
    **Season 1 (Cool–Dry):** Early June 2025 → Winter  
    **Season 2 (Wet–Cool):** Mid-September 2025 → Spring  

    **Substrates sampled (where present):**  
    - Macroplastic debris: bottles, plastic bags, plastic wrappers  
    - Natural substrates: Coarse substrates (pebbles, cobbles) and vegetation
    """)

    # Data Analysis
    st.markdown("### Data Analysis")
    st.markdown("""
    - Shapiro–Wilk test for normality  
    - Paired t-test and Wilcoxon signed-rank tests  
    - PCA for environmental variables  
    - Shannon–Wiener, Simpson, and species richness indices  
    - PERMANOVA and SIMPER for community comparisons  
    """)


# --- RESULTS ---
elif menu == "Results":
    st.subheader("Results")

    # 1. Environmental Variables
    st.markdown("## 1. Environmental Variables")
    st.image("PCA_Biplot.png", use_container_width=True)
    st.markdown("""
    PCA explained 68.1% of the variance in environmental variables.
    A clear separation between the two seasons was observed.  
    **Season 1 (S1, winter)** exhibited greater variability in physio-chemical conditions,  
    while **Season 2 (S2, spring)** maintained more stable conditions.
    """)

    # Table 1: Seasonal Water Quality Comparison
    st.markdown("### Table 1: Statistical results for seasonal water quality comparison")
    table1_html = """
    <table style="width:90%; border-collapse: collapse; font-size:12px;">
        <tr style="background-color:#f2f2f2;">
            <th style="border:1px solid black; padding:3px;">Variable</th>
            <th style="border:1px solid black; padding:3px;">Test Statistics</th>
            <th style="border:1px solid black; padding:3px;">p-value</th>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:3px; color:blue;">Temp</td>
            <td style="border:1px solid black; padding:3px;">t = -9.44</td>
            <td style="border:1px solid black; padding:3px; color:red; font-weight:bold;">p = 0.001953 P<0.05</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:3px; color:blue;">pH</td>
            <td style="border:1px solid black; padding:3px;">Z = 2.6656</td>
            <td style="border:1px solid black; padding:3px; color:red; font-weight:bold;">p = 0.0039063 P<0.05</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:3px; color:blue;">TDS</td>
            <td style="border:1px solid black; padding:3px;">t = -6.044</td>
            <td style="border:1px solid black; padding:3px; color:red; font-weight:bold;">p = 0.0019531 P<0.05</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:3px; color:blue;">ORP</td>
            <td style="border:1px solid black; padding:3px;">Z = 1.78</td>
            <td style="border:1px solid black; padding:3px;">p = 0.083984</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:3px; color:blue;">%DO</td>
            <td style="border:1px solid black; padding:3px;">Z = 17838</td>
            <td style="border:1px solid black; padding:3px;">p = 0.083984</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:3px; color:blue;">EC</td>
            <td style="border:1px solid black; padding:3px;">t = -1.9245</td>
            <td style="border:1px solid black; padding:3px;">p = 0.0855938</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:3px; color:blue;">Phosphorus</td>
            <td style="border:1px solid black; padding:3px;">t = -1.1851</td>
            <td style="border:1px solid black; padding:3px;">p = 0.249</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:3px; color:blue;">P Pentoxide</td>
            <td style="border:1px solid black; padding:3px;">t = -1.356</td>
            <td style="border:1px solid black; padding:3px;">p = 0.19922</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:3px; color:blue;">Phosphate</td>
            <td style="border:1px solid black; padding:3px;">t = -1.66</td>
            <td style="border:1px solid black; padding:3px;">p = 0.166</td>
        </tr>
    </table>
    """
    st.markdown(table1_html, unsafe_allow_html=True)

    # 2. Species Composition
    st.markdown("## 2. Species Composition")
    st.markdown("""
    *4,157 individuals* were collected in S1 and *604 individuals* in S2.
    - S1: Natural (2,232), Plastics (1,916)  
    - S2: Natural (181), Plastics (423)  
    """)

    # 3. Taxonomic Diversity
      # Diversity indices images
    st.markdown("## 3. Taxonomic Diversity")
    col1, col2, col3 = st.columns(3)
    
    try:
        col1.image("Abundance1.png", caption="Abundance", use_container_width=True)
    except:
        col1.warning("Abundance1.png not found")
    
    try:
        col2.image("Evenness5.png", caption="Evenness", use_container_width=True)
    except:
        col2.warning("Evenness5.png not found")
    
    try:
        col3.image("Shannon2.png", caption="Shannon Index", use_container_width=True)
    except:
        col3.warning("Shannon2.png not found")

    col4, col5 = st.columns(2)
    
    try:
        col4.image("Simpson4.png", caption="Simpson Index", use_container_width=True)
    except:
        col4.warning("Simpson4.png not found")
    
    try:
        col5.image("Species_richness3.png", caption="Species Richness", use_container_width=True)
    except:
        col5.warning("Species_richness3.png not found")

    # Table 2: Diversity indices
    st.markdown("### Table 2: Significance of Macroinvertebrate Diversity Indices Between Substrates and Seasons")
    table2_html = """
    <table style="width:90%; border-collapse: collapse; font-size:12px;">
        <tr style="background-color:#f2f2f2;">
            <th style="border:1px solid black; padding:3px;">Diversity indices</th>
            <th style="border:1px solid black; padding:3px;">Substrates</th>
            <th style="border:1px solid black; padding:3px;">Seasons</th>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:3px; color:blue;">Abundance</td>
            <td style="border:1px solid black; padding:3px;">0.38318 (P>0.05)</td>
            <td style="border:1px solid black; padding:3px; color:red; font-weight:bold;">0.0016899 (P<0.05)</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:3px; color:blue;">Species richness</td>
            <td style="border:1px solid black; padding:3px;">0.17626 (P>0.05)</td>
            <td style="border:1px solid black; padding:3px; color:red; font-weight:bold;">0.00011253 (P<0.05)</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:3px; color:blue;">Evenness</td>
            <td style="border:1px solid black; padding:3px;">0.30899 (P>0.05)</td>
            <td style="border:1px solid black; padding:3px;">0.14237 (P>0.05)</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:3px; color:blue;">Simpson diversity</td>
            <td style="border:1px solid black; padding:3px; color:red; font-weight:bold;">0.0136 (P<0.05)</td>
            <td style="border:1px solid black; padding:3px;">0.064322 (P>0.05)</td>
        </tr>
        <tr>
            <td style="border:1px solid black; padding:3px; color:blue;">Shannon</td>
            <td style="border:1px solid black; padding:3px; color:red; font-weight:bold;">0.0106 (P<0.05)</td>
            <td style="border:1px solid black; padding:3px; color:red; font-weight:bold;">0.0068626 (P<0.05)</td>
        </tr>
    </table>
    """
    st.markdown(table2_html, unsafe_allow_html=True)

    # Additional diversity interpretation
    st.markdown("""
    Evenness and Simpson diversity did not differ significantly between the two seasons.  
    Simpson diversity showed significant variation in substrates (<span style="color:red; font-weight:bold;">P<0.05</span>).
    """, unsafe_allow_html=True)

    # 4. Datasets (Excel)
    st.markdown("## 4. Datasets (Excel)")
    try:
        df_macro = pd.read_excel("Macroinvertebrates_Season1_2.xlsx")
        df_water = pd.read_excel("Water_Parameters_Season1_2.xlsx")
        df_div = pd.read_excel("Diversity_Indices.xlsx")

        st.write("### Macroinvertebrates Data")
        st.dataframe(df_macro, use_container_width=True)
        st.download_button(
            label="Download Macroinvertebrates Data",
            data=open("Macroinvertebrates_Season1_2.xlsx", "rb").read(),
            file_name="Macroinvertebrates_Season1_2.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        st.write("### Water Parameters Data")
        st.dataframe(df_water, use_container_width=True)
        st.download_button(
            label="Download Water Parameters Data",
            data=open("Water_Parameters_Season1_2.xlsx", "rb").read(),
            file_name="Water_Parameters_Season1_2.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        st.write("### Diversity Indices Data")
        st.dataframe(df_div, use_container_width=True)
        st.download_button(
            label="Download Diversity Indices Data",
            data=open("Diversity_Indices.xlsx", "rb").read(),
            file_name="Diversity_Indices.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"Excel dataset not found or failed to load. Error: {e}")

    # 5. PERMANOVA & SIMPER
    st.markdown("## 5. PERMANOVA & SIMPER Results")
    perm_html = """
    <ul>
        <li><strong>PERMANOVA</strong>
            <ul>
                <li><span style="color:blue;">Substrate:</span> Not significant (<span style="color:red; font-weight:bold;">p = 0.711</span>, F = 0.820)</li>
                <li><span style="color:blue;">Season:</span> Highly significant (<span style="color:red; font-weight:bold;">p = 0.001</span>, F = 2.369)</li>
                <li><span style="color:blue;">Substrate × Season:</span> Significant (<span style="color:red; font-weight:bold;">p = 0.017</span>, F = 1.443)</li>
            </ul>
        </li>
        <li><strong>SIMPER</strong>
            <ul>
                <li>Chironominae: 21.4% of dissimilarity, plastics (52.6%) & natural substrates (32.3%)</li>
                <li>Tanypodinae: 15.4% dissimilarity, natural substrates (52%) & plastics (16.9%)</li>
                <li>Marsupiobdella africana, Stenophysa marmota, and Culicine: &lt;1% each</li>
            </ul>
        </li>
    </ul>
    """
    st.markdown(perm_html, unsafe_allow_html=True)



# --- DISCUSSION ---
elif menu == "Discussion":
    st.subheader("Discussion")

    st.markdown("""
    <p><strong style="color:black;">
    Cause of dramatic seasonal decline in macroinvertebrates
    </strong></p>

    <p><strong style="color:blue;">Life Cycle Patterns:</strong><br>
    Many aquatic insects have synchronized life cycles. The high abundance in S1 (cool-dry)
    likely reflects mature larvae before emerging as flying adults.<br>
    The low abundance in S2 (wet-cool) suggests that most larvae had already emerged,
    leaving only a few individuals.
    </p>

    <p><strong style="color:blue;">Physical Disturbance:</strong><br>
    Rainfall occurring a week prior to sampling likely increased river flow and displaced organisms.<br>
    Higher flows during the wet season can sweep macroinvertebrates off natural substrates.
    </p>

    <p><strong style="color:black;">
    Causes of plastics supporting more diversity in Season 2
    </strong></p>

    <p><strong style="color:blue;">Habitat Stability &amp; Complexity:</strong><br>
    During high-flow events, natural substrates such as leaves and small rocks are easily displaced.<br>
    Macroplastics provide more stable refuges during disturbances due to their size,
    durability, and ability to become lodged within the river channel.
    </p>
    """, unsafe_allow_html=True)

# --- CONCLUSION ---
elif menu == "Conclusion":
    st.subheader("Conclusion")
    
    st.markdown("""
    ### Main Conclusions
    
    #### 1. Habitat Function Confirmed
    ✅ Macroplastics provide viable habitats for aquatic macroinvertebrates  
    ✅ Comparable community structure to natural substrates
    
    #### 2. Seasonal Dynamics
    ✅ Significant seasonal variation in colonization patterns  
    ✅ Macroplastics more important during high-flow conditions
    
    #### 3. Management Implications
    ⚠️ Plastic pollution has complex ecological roles  
    ⚠️ Removal strategies should consider habitat function  
    ⚠️ Need for integrated pollution management
    """)
    
    st.info("""
    **Recommendations:**
    1. Consider ecological functions in plastic pollution management
    2. Monitor plastic habitats in conservation planning
    3. Further research on long-term impacts
    """)


# --- ACKNOWLEDGMENTS ---
elif menu == "Acknowledgments":
    st.subheader("Acknowledgments")
    st.markdown("""
    I would like to sincerely thank the University of Mpumalanga for providing
    the academic support and resources necessary to complete this Honours study.
    Special thanks to the Aquatic Systems Research Group (ASRG) coordinated by Dr Tatenda Dalu,
    and thanks to my supervisor Dr Pule MPopetsi for guidance during fieldwork and laboratory analysis.
    I am also grateful to the National Research Foundation (NRF) for funding support, and
    to all colleagues and friends who assisted with data collection, processing, and thoughtful discussions throughout the project.
    """)

    # Logos
    col1, col2 = st.columns(2)
    col1.image("UMP_Logo.png", caption="University of Mpumalanga", use_container_width=True)
    col2.image("NRF_Logo.png", caption="National Research Foundation", use_container_width=True)

    # QR codes for ASRG website & Facebook
    urls = {
        "ASRG Facebook": "https://www.facebook.com/AquaticSystemsResearchGroup",
        "ASRG Website": "http://www.aquasystems-res.com"
    }

    for name, url in urls.items():
        qr = qrcode.QRCode(box_size=4)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buf = BytesIO()
        img.save(buf, format="PNG")
        st.image(buf, caption=f"Scan QR Code for {name}")

# --- REFERENCES ---
elif menu == "References":
    st.subheader("References")
    st.markdown("""
    Azevedo-Santos, V.M., et al. (2021). Plastic pollution: A focus on freshwater biodiversity. Ambio  
    Blettler, M.C.M., et al. (2018). Freshwater plastic pollution: Recognizing research biases. Water Research  
    Dalu, T., et al. (2025). Macroplastic colonization by aquatic invertebrates in African rivers. Scientific Reports  
    Hoellein, T.J., et al. (2014). Anthropogenic litter in urban freshwater ecosystems. PLOS One  
    Amaral-Zettler, L.A., Zettler, E.R. and Mincer, T.J., 2020. Ecology of the plastisphere. Nature Reviews Microbiology  
    Rummel, C.D., et al. (2021). Effects of polymer type on colonization. Environmental Science & Technology  
    Gallitelli, L., et al. (2023). Seasonal dynamics of plastic colonization.. Science of the Total Environment  
    Marino, F., et al. (2024). Comparative analysis of natural and artificial substrate communities. Water  

    """)

# --- FOOTER ---
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)
with footer_col1:
    st.caption("© 2025 Venerate Mdaka")
with footer_col2:
    st.caption("University of Mpumalanga")
with footer_col3:
    st.caption("BSc Honours Research Project")













