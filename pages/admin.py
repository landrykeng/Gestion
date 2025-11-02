import streamlit as st
import pandas as pd
from datetime import datetime, date, time, timedelta
import os
import datetime
import random
from Fonction import *
from Authentification import *


# Configuration de la page


# CSS personnalisé pour l'interface admin
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #8b0000 0%, #dc143c 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    
    .admin-info {
        background: linear-gradient(135deg, #dc143c 0%, #ff6b6b 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .form-container {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
        border-left: 4px solid #dc143c;
    }
    
    .success-box {
        background: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
    
    .error-box {
        background: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #f5c6cb;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: #fff3cd;
        color: #856404;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #ffeaa7;
        margin: 1rem 0;
    }
    
    .info-box {
        background: #d1ecf1;
        color: #0c5460;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #bee5eb;
        margin: 1rem 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #dc143c 0%, #ff6b6b 100%);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 1rem;
    }
    
    .login-container {
        background: white;
        padding: 3rem;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        max-width: 500px;
        margin: 2rem auto;
        border-top: 5px solid #dc143c;
    }
    
    .teacher-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #dc143c;
        margin-bottom: 1rem;
    }
    
    .payroll-card {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1rem;
    }
    
    .danger-zone {
        background: #f8d7da;
        padding: 1rem;
        border-radius: 8px;
        border: 2px solid #dc3545;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)


# CSS personnalisé
management_css = """
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    
    .form-container {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 2rem;
        border-left: 4px solid #1e3c72;
    }
    
    .success-box {
        background: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
    
    .error-box {
        background: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #f5c6cb;
        margin: 1rem 0;
    }
    
    .info-box {
        background: #d1ecf1;
        color: #0c5460;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #bee5eb;
        margin: 1rem 0;
    }
    
    .warning-box {
        background: #fff3cd;
        color: #856404;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #ffeaa7;
        margin: 1rem 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 1rem;
    }
    
    .data-table {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .student-profile {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    
    .search-container {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        border: 2px solid #1e3c72;
    }
    
    .receipt-container {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 2rem 0;
        border: 2px solid #28a745;
    }
    
    .absent-student-card {
        background: #f8d7da;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #dc3545;
        margin-bottom: 1rem;
    }
</style>
"""

table_css = """
<style>
/* Style général des tableaux */
.stDataFrame {
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    border-radius: 10px;
    overflow: hidden;
}

/* En-tête du tableau */
.stDataFrame thead {
    background-color: #1e3c72;
    color: white;
    font-weight: bold;
}

/* Lignes du tableau */
.stDataFrame tbody tr:nth-child(even) {
    background-color: #f8f9fa;
}

.stDataFrame tbody tr:nth-child(odd) {
    background-color: #ffffff;
}

/* Effet de survol */
.stDataFrame tbody tr:hover {
    background-color: #e9ecef;
    transition: background-color 0.3s ease;
}

/* Cellules */
.stDataFrame th, .stDataFrame td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #dee2e6;
}

/* Style des colonnes */
.stDataFrame th {
    text-transform: uppercase;
    font-size: 0.9em;
    letter-spacing: 1px;
}
</style>
"""

  

def main():
    st.markdown(table_css, unsafe_allow_html=True)
    st.markdown(management_css, unsafe_allow_html=True)
    
    is_authenticated = authentication_system("Administrateur")
    
    if is_authenticated:
        
        #st.set_page_config(
            #page_title="Admin - STATO-SPHERE PREPAS",
            #page_icon="⚡",
            #layout="wide",
            #initial_sidebar_state="expanded")
        
        user = st.session_state['username']
        id_center_dict=st.session_state.dict_ens
        #user_center=id_center_dict[user][1]
        user_center="Yaoundé"
        etudiants_df=st.session_state.etudiants_df
        enseignants_df=st.session_state.enseignants_df
        seances_df=st.session_state.seances_df
        depenses_df=st.session_state.depenses_df
        versements_df=st.session_state.versements_df
        ventes_df=st.session_state.ventes_df
        presence_df=st.session_state.presence_df
        fiches_paie_df=st.session_state.fiches_paie_df
        Connect_df=st.session_state.Connect_df

        
        #etudiants_df=etudiants_df[etudiants_df["Centre"]==user_center]
        #depenses_df=depenses_df[depenses_df["CentreResponsable"]==user_center]
        #versements_df=versements_df[versements_df["Centre"]==user_center]
        #ventes_df=ventes_df[ventes_df["Centre"]==user_center]
        #presence_df=presence_df[presence_df["Centre"]==user_center]
        
        st.markdown(f"""
            <div class="admin-info">
                <h2>⚡ Espace Administrateur</h2>
                <p><strong>Connecté en tant que :</strong> {user.upper()}</p>
                <p><strong>Droits :</strong> Accès complet à toutes les fonctionnalités</p>
            </div>
            """, unsafe_allow_html=True)
        

            
        #etudiants_df, enseignants_df, seances_df, depenses_df, versements_df, ventes_df, presence_df, presences_df, fiches_paie_df, Connect_df=load_all_data()
        
        
        
        
        # Interface à onglets
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
            "👨‍🏫 Enseignants", "👥 Étudiants", "💸 Dépenses", "💰 Versements", 
            "📚 Ventes", "📋 Présences", "💵 Fiches de Paie","Données"
        ])
    
        # ==================== ONGLET ENSEIGNANTS ====================
        with tab1:
            st.markdown("## 👨‍🏫 Gestion des Enseignants")
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown("### ➕ Ajouter un Nouvel Enseignant")
                
                with st.form("form_enseignant"):
                    col_a, col_b = st.columns(2)
                    
                    with col_a:
                        nom_ens = st.text_input("Nom *", placeholder="Ex: MBANG")
                        prenom_ens = st.text_input("Prénom *", placeholder="Ex: Pierre")
                        matiere_ens = st.multiselect("Matières enseignées *", COURS_CHOICES)
                        statut_ens = st.selectbox("Statut *", STATUT_ENSEIGNANT_CHOICES)
                    
                    with col_b:
                        telephone_ens = st.text_input("Téléphone", placeholder="Ex: +237670123456")
                        centre_ens = st.multiselect("Centres d'affectation *", CENTRES_CHOICES)
                        date_embauche = st.date_input("Date d'embauche *", value=date.today())
                    
                    submitted_ens = st.form_submit_button("👨‍🏫 Ajouter l'Enseignant", type="primary")
                    
                    if submitted_ens:
                        if nom_ens and prenom_ens and matiere_ens and statut_ens and centre_ens:
                            id_enseignant = len(enseignants_df) + 1
                            
                            data = [ nom_ens, prenom_ens, 
                                ", ".join(matiere_ens), telephone_ens, statut_ens
                            ]
                            
                            if save_to_supabase("Enseignants", data):
                                #=====Génération des identifiants de l'enseignant
                                users = load_users()
        
                                # Parcourir les lignes du DataFrame
                                username = nom_ens
                                status_pour_compte = "Enseignant"
                                password = nom_ens[:3]+ str(random.randint(100,999))

                                    # Si l'utilisateur n'existe pas déjà, l'ajouter
                                if username not in users["users"]:
                                        users["users"][username] = {
                                            "password": hash_password(password),
                                            "status": status_pour_compte,
                                            "email": f"{username}@example.com",  # Email par défaut
                                            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                        }
                                
                                # Sauvegarder la base d'utilisateurs mise à jour
                                save_users(users)
                                #=======================================
                                st.session_state.enseignants_df = read_from_supabase("Enseignants")
                                st.markdown(f"""
                                <div class="success-box">
                                    ✅ <strong>Enseignant ajouté avec succès !</strong><br>
                                    Nom: <strong>{nom_ens} {prenom_ens}</strong><br>
                                    Statut: <strong>{statut_ens}</strong><br>
                                    Mot de passe: <strong>{password}</strong> 
                                </div>
                                """, unsafe_allow_html=True)
                                st.balloons()
                            else:
                                st.markdown("""
                                <div class="error-box">
                                    ❌ Erreur lors de l'ajout.
                                </div>
                                """, unsafe_allow_html=True)
                        else:
                            st.markdown("""
                            <div class="error-box">
                                ⚠️ Veuillez remplir tous les champs obligatoires
                            </div>
                            """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown("#### Honnoraires suivant les statuts")
                st.dataframe(statut_df,hide_index=True)
            # Liste des enseignants
            if not enseignants_df.empty:
                st.markdown("---")
                st.markdown("### 📋 Liste des Enseignants")
                
                for idx, ens in enseignants_df.iterrows():
                    st.markdown(f"""
                    <div class="teacher-card">
                        <h4>👨‍🏫 {ens['Nom']} {ens['Prénom']}</h4>
                        <p><strong>📚 Matières:</strong> {ens['Matière']} | 
                        <strong>👔 Statut:</strong> {ens['statut']} | 
                        <strong>💰 Taux:</strong> {ens.get('TauxHoraire', 'N/A')} FCFA/h</p>
                        <p><strong>📍 Centres:</strong> {ens.get('Centre', 'N/A')} | 
                        <strong>📞 Tel:</strong> {ens.get('Téléphone', 'N/A')}</p>
                    </div>
                    """, unsafe_allow_html=True)
        
        # ==================== ONGLET ÉTUDIANTS ====================
        with tab2:
            st.markdown("## 👥 Gestion des Étudiants")
            
            col1, col2 = st.columns([2, 2])
            
            with col1:
                st.markdown("### ➕ Enregistrer un Nouvel Étudiant")
                
                with st.form("form_etudiant"):
                    col_a, col_b = st.columns([1,2])
                    
                    with col_a:
                        nom = st.text_input("Nom *", placeholder="Ex: DUPONT")
                        prenom = st.text_input("Prénom *", placeholder="Ex: Jean")
                        sexe = st.selectbox("Sexe *", SEXE_CHOICES)
                        concours1 = st.selectbox("Concours Principal *", CONCOURS_CHOICES)
                        etablissement = st.selectbox("Établissement *", ETABLISSEMENT)
                        if etablissement == "Autre":
                            #st.rerun()
                            etablissement = st.text_input("Veuillez préciser l'établissement :")
                        centre = st.selectbox("Centre *", CENTRES_CHOICES)
                    
                    with col_b:
                        date_arrivee = st.date_input("Date d'arrivée *", value=date.today())
                        concours2 = st.selectbox("Concours Secondaire (optionnel)", [""] + CONCOURS_CHOICES)
                        concours3 = st.selectbox("Concours Tertiaire (optionnel)", [""] + CONCOURS_CHOICES)
                        telephone = st.text_input("Téléphone", placeholder="Ex: +237670123456")
                    
                    submitted = st.form_submit_button("🎓 Enregistrer l'Étudiant", type="primary")
                    
                    if submitted:
                        if nom and prenom and sexe and concours1 and centre:
                            matricule = generate_matricule()
                            
                            data = [
                                matricule, nom, prenom, sexe, concours1,
                                concours2 if concours2 else "", concours3 if concours3 else "",
                                telephone,  etablissement, centre,date_arrivee.strftime('%Y-%m-%d')
                            ]
                            
                            if save_to_supabase("Etudiants", data):
                                st.session_state.etudiants_df = read_from_supabase("Etudiants")
                                st.markdown(f"""
                                <div class="success-box">
                                    ✅ <strong>Étudiant enregistré avec succès !</strong><br>
                                    Matricule généré: <strong>{matricule}</strong>
                                </div>
                                """, unsafe_allow_html=True)
                                st.balloons()
                            else:
                                st.markdown("""
                                <div class="error-box">
                                    ❌ Erreur lors de l'enregistrement. Veuillez réessayer.
                                </div>
                                """, unsafe_allow_html=True)
                        else:
                            st.markdown("""
                            <div class="error-box">
                                ⚠️ Veuillez remplir tous les champs obligatoires (*)
                            </div>
                            """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown("## 🔍 Recherche et Profil Étudiant")
            
                st.markdown('<div class="search-container">', unsafe_allow_html=True)
                st.markdown("### 🔍 Rechercher un Étudiant")
                
                # Barre de recherche
                search_query = st.text_input(
                    "🔍 Tapez le nom, prénom ou matricule de l'étudiant",
                    placeholder="Ex: DUPONT ou Jean ou STAT20250101ABCD",
                    key="student_search"
                )
                
                if search_query:
                    # Effectuer la recherche
                    search_results = search_student(search_query, etudiants_df)
                    
                    if not search_results.empty:
                        st.markdown(f"### 📋 Résultats de la recherche ({len(search_results)} trouvé(s))")
                        
                        # Afficher les résultats sous forme de sélection
                        for idx, student in search_results.iterrows():
                            if st.button(f"👤 {student['Nom']} {student['Prénom']} - {student['Matricule']}", key=f"select_{idx}"):
                                st.session_state['selected_student'] = student
                                st.rerun()
                    else:
                        st.warning("🚫 Aucun étudiant trouvé avec cette recherche")
                
                st.markdown('</div>', unsafe_allow_html=True)
                
            # Affichage du profil de l'étudiant sélectionné
            if 'selected_student' in st.session_state:
                    student = st.session_state['selected_student']
                    
                    # Calcul des statistiques de l'étudiant
                    #presences_df = read_from_supabase("Présences")
                    stats = calculate_student_stats(student['Matricule'], versements_df, presence_df, seances_df)
                    
                    st.markdown("---")
                    st.markdown(f"""
                    <div class="student-profile">
                        <h2>👤 Profil de {student['Nom']} {student['Prénom']}</h2>
                        <p><strong>Matricule:</strong> {student['Matricule']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Informations personnelles
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.markdown("#### 📋 Informations Personnelles")
                        st.write(f"**Nom:** {student['Nom']}")
                        st.write(f"**Prénom:** {student['Prénom']}")
                        st.write(f"**Sexe:** {student['Sexe']}")
                        st.write(f"**Téléphone:** {student.get('Téléphone', 'Non renseigné')}")
                        st.write(f"**Centre:** {student['Centre']}")
                        st.write(f"**Établissement:** {student.get('Etablissement', 'Non renseigné')}")
                        st.write(f"**Date d'arrivée:** {student['DateArrivée']}")
                    
                    with col2:
                        st.markdown("#### 🎓 Concours Préparés")
                        st.write(f"**Principal:** {student['Concours1']}")
                        #if student.get('Concours2'):
                            #st.write(f"**Secondaire:** {student['Concours2']}")
                        #if student.get('Concours3'):
                            #st.write(f"**Tertiaire:** {student['Concours3']}")
                        
                        st.markdown("#### 💰 Finances")
                        st.write(f"**Total versé:** {stats['total_verse']:,.0f} FCFA")
                        st.write(f"**Nombre de versements:** {stats['nombre_versements']}")
                    
                    with col3:
                        st.markdown("#### 📊 Assiduité")
                        st.write(f"**Total séances:** {stats['total_seances']}")
                        st.write(f"**Présences:** {stats['seances_presentes']}")
                        st.write(f"**Absences:** {stats['seances_absentes']}")
                        st.write(f"**Retards:** {stats['seances_retard']}")
                        
                        if stats['total_seances'] > 0:
                            if stats['taux_absenteisme'] <= 10:
                                st.success(f"**Taux d'absentéisme:** {stats['taux_absenteisme']:.1f}% 🟢")
                            elif stats['taux_absenteisme'] <= 25:
                                st.warning(f"**Taux d'absentéisme:** {stats['taux_absenteisme']:.1f}% 🟡")
                            else:
                                st.error(f"**Taux d'absentéisme:** {stats['taux_absenteisme']:.1f}% 🔴")
                        else:
                            st.info("**Taux d'absentéisme:** Aucune séance enregistrée")
                    
                    # Bouton pour effacer la sélection
                    if st.button("🗑️ Effacer la sélection"):
                        del st.session_state['selected_student']
                        st.rerun()
        
        # ==================== ONGLET DÉPENSES ====================
        with tab3:
            st.markdown("## 💸 Gestion des Dépenses")
            
            st.markdown('<div class="form-container">', unsafe_allow_html=True)
            st.markdown("### ➕ Enregistrer une Nouvelle Dépense")
            
            with st.form("form_depense"):
                col_a, col_b = st.columns(2)
                
                with col_a:
                    motif_depense = st.text_input("Motif de la dépense *", placeholder="Ex: Achat de matériel")
                    type_depense = st.selectbox("Type de dépense *", TYPE_DEPENSE_CHOICES)
                    centre_responsable = st.selectbox("Centre responsable *", CENTRES_CHOICES)
                
                with col_b:
                    date_depense = st.date_input("Date *", value=date.today())
                    centre_beneficiaire = st.multiselect("Centre bénéficiaire *", CENTRES_CHOICES)
                    montant = st.number_input("Montant (FCFA) *", min_value=0, step=1000)
                
                submitted_depense = st.form_submit_button("💳 Enregistrer", type="primary")
                All_beneficiaire = "; ".join(centre_beneficiaire)
                if submitted_depense:
                    if motif_depense and type_depense and montant > 0:
                        id_depense = len(depenses_df) + 1
                        data = [motif_depense, type_depense, date_depense.strftime('%Y-%m-%d'),
                            centre_responsable, All_beneficiaire, montant
                        ]
                        
                        if save_to_supabase("Dépenses", data):
                            st.session_state.depenses_df = read_from_supabase("Dépenses")
                            st.success(f"✅ Dépense de {montant:,} FCFA enregistrée")
                        else:
                            st.error("❌ Erreur lors de l'enregistrement")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # ==================== ONGLET VERSEMENTS ====================
        with tab4:
            st.markdown('## <div class="form-container"> 💰 Gestion des Versements', unsafe_allow_html=True)
            col1, col2 = st.columns([2, 1])
            
            with col1:
                
                st.markdown("### ➕ Enregistrer un Nouveau Versement")
                
                with st.form("form_versement"):
                    col_a, col_b = st.columns(2)
                
                    with col_a:
                        if not etudiants_df.empty:
                            etudiants_list = [f"{row['Matricule']} - {row['Nom']} {row['Prénom']}" 
                                            for _, row in etudiants_df.iterrows()]
                            etudiant_selectionne = st.selectbox("Étudiant *", etudiants_list)
                            matricule_etudiant = etudiant_selectionne.split(" - ")[0] if etudiant_selectionne else ""
                        else:
                            matricule_etudiant = ""
                        montant_versement = st.number_input("Montant (FCFA) *", min_value=0, step=1000)
                        date_versement = st.date_input("Date *", value=date.today())
                    
                    with col_b:
                        centre_versement = st.selectbox("Centre *", CENTRES_CHOICES)
                        motif_versement = st.text_input("Motif", placeholder="Ex: Frais d'inscription")
                    
                    submitted_versement = st.form_submit_button("💵 Enregistrer le Versement", type="primary")
                    
                    if submitted_versement:
                        if date_versement and montant_versement > 0 and matricule_etudiant and centre_versement:
                            id_versement = len(versements_df) + 1
                            
                            data = [date_versement.strftime('%Y-%m-%d'), motif_versement,
                                centre_versement, montant_versement, matricule_etudiant
                            ]
                            
                            if save_to_supabase("Versement", data):
                                st.session_state.versements_df = read_from_supabase("Versement")
                                st.markdown(f"""
                                <div class="success-box">
                                    ✅ <strong>Versement enregistré avec succès !</strong><br>
                                    Montant: <strong>{montant_versement:,.0f} FCFA</strong>
                                </div>
                                """, unsafe_allow_html=True)
                                
                                # Générer le reçu
                                student_info = etudiants_df[etudiants_df['Matricule'] == matricule_etudiant].iloc[0]
                                versement_info = {
                                    'date': date_versement.strftime('%d/%m/%Y'),
                                    'montant': montant_versement,
                                    'motif': motif_versement
                                }
                                
                                receipt_html = generate_receipt_html(student_info, versement_info)
                                
                                st.markdown("---")
                                st.markdown("### 📄 Reçu de Paiement")
                                
                                col_receipt1, col_receipt2 = st.columns([3, 1])
                                
                                with col_receipt1:
                                    st.markdown(f"""
                                    <div class="receipt-container">
                                        <h4>🎓 Reçu généré automatiquement</h4>
                                        <p><strong>Étudiant:</strong> {student_info['Nom']} {student_info['Prénom']}</p>
                                        <p><strong>Matricule:</strong> {student_info['Matricule']}</p>
                                        <p><strong>Montant:</strong> {montant_versement:,.0f} FCFA</p>
                                        <p><strong>Date:</strong> {date_versement.strftime('%d/%m/%Y')}</p>
                                    </div>
                                    """, unsafe_allow_html=True)
                                
                                with col_receipt2:
                                    # Bouton de téléchargement du reçu
                                    b64 = base64.b64encode(receipt_html.encode()).decode()
                                    href = f'data:text/html;base64,{b64}'
                                    st.markdown(f'<a href="{href}" download="recu_{matricule_etudiant}_{date_versement.strftime("%Y%m%d")}.html"><button style="background-color: #28a745; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">📥 Télécharger le Reçu</button></a>', unsafe_allow_html=True)
                            else:
                                st.markdown("""
                                <div class="error-box">
                                    ❌ Erreur lors de l'enregistrement.
                                </div>
                                """, unsafe_allow_html=True)
                        else:
                            st.markdown("""
                            <div class="error-box">
                                ⚠️ Veuillez remplir tous les champs obligatoires
                            </div>
                            """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                pass
        
        # ==================== ONGLET VENTES ====================
        with tab5:
            st.markdown("## 📚 Gestion des Ventes de Bords")
            
            st.markdown('<div class="form-container">', unsafe_allow_html=True)
            
            with st.form("form_vente"):
                col_a, col_b = st.columns(2)
                
                with col_a:
                    date_vente = st.date_input("Date *", value=date.today())
                    bord_vendu = st.selectbox("Bords vendus *", [f"Bords de {c}" for c in CONCOURS_CHOICES])
                    nom_acheteur = st.text_input("Nom de l'acheteur *")
                
                with col_b:
                    nombre_bords = st.number_input("Nombre d'exemplaires *", min_value=1, value=1)
                    montant_vente = st.number_input("Montant total (FCFA) *", min_value=0, step=500)
                    contact_acheteur = st.text_input("Contact acheteur")
                
                centre_vente = st.selectbox("Centre *", CENTRES_CHOICES)
                
                submitted_vente = st.form_submit_button("📖 Enregistrer", type="primary")
                
                if submitted_vente:
                    if date_vente and bord_vendu and nom_acheteur and montant_vente > 0:
                        id_vente = len(ventes_df) + 1
                        data = [bord_vendu, nom_acheteur, contact_acheteur,
                            nombre_bords, montant_vente, centre_vente, date_vente.strftime('%Y-%m-%d')
                        ]
                        
                        if save_to_supabase("Bord", data):
                            st.session_state.ventes_df = read_from_supabase("Bord")
                            st.success(f"✅ Vente de {montant_vente:,} FCFA enregistrée")
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # ==================== ONGLET PRÉSENCES ====================
        with tab6:
            st.markdown("## 📋 Gestion des Présences - Appel Interactif")
            
            # Initialisation des variables de session pour l'appel
            if "appel_started" not in st.session_state:
                st.session_state.appel_started = False
            if "current_student_index" not in st.session_state:
                st.session_state.current_student_index = 0
            if "presences_data" not in st.session_state:
                st.session_state.presences_data = {}
            if "etudiants_appel" not in st.session_state:
                st.session_state.etudiants_appel = []
            
            st.markdown('<div class="form-container">', unsafe_allow_html=True)
            
            if not st.session_state.appel_started:
                # === PHASE 1: Configuration de l'appel ===
                st.markdown("### ⚙️ Configuration de l'Appel")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    centre_appel = st.selectbox("📍 Centre *", CENTRES_CHOICES, key="centre_config")
                    
                    # Sélection multiple des concours
                    concours_appel = st.multiselect(
                        "🎓 Concours *", 
                        CONCOURS_CHOICES, 
                        default=[CONCOURS_CHOICES[0]],
                        key="concours_config"
                    )
                    
                    # Liste des enseignants (ici on peut lire depuis Excel ou avoir une liste prédéfinie)
                    enseignants_list = [
                        "Dr. MBANG Pierre", "Prof. NJOYA Marie", "M. FOMBA Jean",
                        "Mme. KAMGA Sylvie", "Dr. TCHOUMI Paul", "Prof. NANA Claire"
                    ]
                    enseignant = st.selectbox("👨‍🏫 Enseignant *", enseignants_df['Nom'].tolist() if not enseignants_df.empty else ["Enseignant Test"], key="enseignant_config")
                
                with col2:
                    # Liste des cours/matières
                    cours_list = [
                        "MATHEMATIQUES", "FRANCAIS", "CULTURE GENERALE", "ECONOMIE",
                        "ANGLAIS", "STATISTIQUES", "COMPTABILITE", "INFORMATIQUE",
                        "DEMOGRAPHIE", "GEOGRAPHIE"
                    ]
                    cours = st.selectbox("📚 Matière/Cours *", cours_list, key="cours_config")
                    
                    intitule_cours = st.text_input(
                        "📝 Intitulé du cours *", 
                        placeholder="Ex: Analyse mathématique - Chapitre 3",
                        key="intitule_config"
                    )
                    
                    date_appel = st.date_input("📅 Date", value=date.today(), key="date_config")
                    heure_debut = st.time_input("🕐 Heure de début", key="heure_config")
                
                # Filtrage des étudiants selon les critères
                if not etudiants_df.empty and centre_appel and concours_appel:
                    etudiants_filtres = etudiants_df[etudiants_df['Centre'] == centre_appel]
                    
                    # Filtrer par concours (OR entre les concours sélectionnés)
                    etudiants_filtres = etudiants_filtres[(etudiants_filtres['Concours1'].isin(concours_appel)) | (etudiants_filtres['concours2'].isin(concours_appel)) | (etudiants_filtres['concours3'].isin(concours_appel))]
                    etudiants_filtres=etudiants_filtres.sort_values(by=["Nom","Prénom"])
                    # Affichage du résumé
                    st.markdown("---")
                    st.markdown("### 📊 Résumé de l'Appel")
                    
                    col_a, col_b, col_c = st.columns(3)
                    with col_a:
                        st.metric("👥 Étudiants à appeler", len(etudiants_filtres))
                    with col_b:
                        st.metric("📍 Centre", centre_appel)
                    with col_c:
                        st.metric("🎓 Concours", len(concours_appel))
                    
                    if len(etudiants_filtres) > 0:
                        st.markdown("**Aperçu des étudiants :**")
                        preview_df = etudiants_filtres[['Nom', 'Prénom', 'Concours1']].head(5)
                        st.dataframe(preview_df, use_container_width=True)
                        
                        if len(etudiants_filtres) > 5:
                            st.caption(f"... et {len(etudiants_filtres) - 5} autres étudiants")
                        
                        # Bouton pour démarrer l'appel
                        if st.button("🚀 Démarrer l'Appel", type="primary", use_container_width=True):
                            if enseignant and cours and intitule_cours:
                                # Sauvegarder les paramètres dans la session
                                st.session_state.appel_config = {
                                    "centre": centre_appel,
                                    "concours": concours_appel,
                                    "enseignant": enseignant,
                                    "cours": cours,
                                    "intitule": intitule_cours,
                                    "date": date_appel,
                                    "heure_debut": heure_debut
                                }
                                st.session_state.etudiants_appel = etudiants_filtres.to_dict('records')
                                st.session_state.appel_started = True
                                st.session_state.current_student_index = 0
                                st.session_state.presences_data = {}
                                st.rerun()
                            else:
                                st.error("⚠️ Veuillez remplir tous les champs obligatoires")
                    else:
                        st.warning("Aucun étudiant trouvé pour les critères sélectionnés")
                else:
                    if etudiants_df.empty:
                        st.warning("Aucun étudiant enregistré dans le système")
            
            else:
                # === PHASE 2: Appel en cours ===
                config = st.session_state.appel_config
                etudiants = st.session_state.etudiants_appel
                current_index = st.session_state.current_student_index
                total_students = len(etudiants)
                
                # En-tête de l'appel
                st.markdown(f"""
                ### 📋 Appel en Cours
                **📚 {config['cours']}** - {config['intitule']}  
                **👨‍🏫 Enseignant:** {config['enseignant']} | **📍 Centre:** {config['centre']} | **📅 Date:** {config['date']}
                """)
                
                # Barre de progression
                progress = current_index / total_students if total_students > 0 else 0
                st.progress(progress, text=f"Étudiant {current_index} sur {total_students}")
                
                if current_index < total_students:
                    # Affichage des 3 étudiants (précédent, actuel, suivant)
                    st.markdown("---")

                    col1, col2 = st.columns(2) 

                    with col1:
                        # Étudiant précédent
                        if current_index > 0:
                            prev_student = etudiants[current_index - 1]
                            prev_status = st.session_state.presences_data.get(prev_student['Matricule'], "")
                            status_icon = "✅" if prev_status == "Présent" else "❌" if prev_status == "Absent" else ""
                            
                            if prev_status == "Présent":
                                st.success(f"{prev_student['Nom']} {prev_student['Prénom']} : {status_icon} {prev_status}") 
                            else:
                                st.error(f"{prev_student['Nom']} {prev_student['Prénom']} : {status_icon} {prev_status}")
                            
                        else:
                            st.markdown("""
                            <div style="background: #f8f9fa; padding: 1rem; border-radius: 8px; text-align: center;">
                                <h5>👤 Précédent</h5>
                                <p><em>Premier étudiant</em></p>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Étudiant en cours
                        current_student = etudiants[current_index]
                        st.warning(f"{current_student['Nom']} {current_student['Prénom']}")
                        # Étudiant suivant
                        if current_index + 1 < total_students:
                            next_student = etudiants[current_index + 1]
                            st.info(f"👤 Suivant: {next_student['Nom']} {next_student['Prénom']} (En attente...)")
                            
                    # Étudiant actuel
                    with col2:
                        pass
                    
                    # Boutons de présence
                    st.markdown("---")
                    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
                    
                    with col_btn1:
                        if st.button("❌ ABSENT", use_container_width=True, type="secondary"):
                            matricule = current_student['Matricule']
                            st.session_state.presences_data[matricule] = "Absent"
                            st.session_state.current_student_index += 1
                            st.rerun()
                    
                    with col_btn2:
                        if st.button("✅ PRÉSENT", use_container_width=True, type="primary"):
                            matricule = current_student['Matricule']
                            st.session_state.presences_data[matricule] = "Présent"
                            st.session_state.current_student_index += 1
                            st.rerun()
                    
                    with col_btn3:
                        if st.button("⚠️ RETARD", use_container_width=True):
                            matricule = current_student['Matricule']
                            st.session_state.presences_data[matricule] = "Retard"
                            st.session_state.current_student_index += 1
                            st.rerun()
                    
                    # Bouton d'abandon
                    st.markdown("---")
                    if st.button("🔙 Abandonner l'appel", type="secondary"):
                        # Reset de l'appel
                        st.session_state.appel_started = False
                        st.session_state.current_student_index = 0
                        st.session_state.presences_data = {}
                        st.session_state.etudiants_appel = []
                        st.rerun()
                
                else:
                    # === PHASE 3: Appel terminé ===
                    st.markdown("### 🎉 Appel Terminé !")
                    
                    # Résumé des présences
                    presents = sum(1 for status in st.session_state.presences_data.values() if status == "Présent")
                    absents = sum(1 for status in st.session_state.presences_data.values() if status == "Absent")
                    retards = sum(1 for status in st.session_state.presences_data.values() if status == "Retard")
                    
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        st.metric("👥 Total", total_students)
                    with col2:
                        st.metric("✅ Présents", presents)
                    with col3:
                        st.metric("❌ Absents", absents)
                    with col4:
                        st.metric("⚠️ Retards", retards)
                    
                    # Tableau récapitulatif
                    st.markdown("### 📊 Récapitulatif des Présences")
                    recap_data = []
                    for etudiant in etudiants:
                        matricule = etudiant['Matricule']
                        status = st.session_state.presences_data.get(matricule, "Non pointé")
                        recap_data.append({
                            "Matricule": matricule,
                            "Nom": etudiant['Nom'],
                            "Prénom": etudiant['Prénom'],
                            "Statut": status
                        })
                    
                    recap_df = pd.DataFrame(recap_data)
                    st.dataframe(recap_df, use_container_width=True)
                    
                    # Boutons d'action
                    col_save, col_restart = st.columns(2)
                    
                    with col_save:
                        if st.button("💾 Enregistrer les Présences", type="primary", use_container_width=True):
                            #presences_df = read_from_supabase("Présences")
                            success_count = 0
                            
                            for matricule, statut in st.session_state.presences_data.items():
                                id_presence = len(presence_df) + success_count + 1
                                data = [matricule, 
                                    f"{config['cours']} - {config['intitule']}", 
                                    statut, 
                                    config['date'].strftime('%Y-%m-%d'), 
                                    id_center_dict[enseignant][0]  # idEnseignant par défaut (à améliorer)
                                ]
                                
                                if save_to_supabase("Présence", data):
                                    success_count += 1
                            
                            if success_count > 0:
                                st.session_state.presence_df = read_from_supabase("Présence")
                                st.success(f"✅ {success_count} présences enregistrées avec succès !")
                                # Reset après sauvegarde
                                st.session_state.appel_started = False
                                st.session_state.current_student_index = 0
                                st.session_state.presences_data = {}
                                st.session_state.etudiants_appel = []
                                st.balloons()
                            else:
                                st.error("❌ Erreur lors de l'enregistrement des présences")
                    
                    with col_restart:
                        if st.button("🔄 Nouvel Appel", use_container_width=True):
                            # Reset pour un nouvel appel
                            st.session_state.appel_started = False
                            st.session_state.current_student_index = 0
                            st.session_state.presences_data = {}
                            st.session_state.etudiants_appel = []
                            st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)
        
     
        with tab7:
            st.markdown("## 💵 Génération des Fiches de Paie")
            
            col1, col2 = st.columns([9, 1])
            
            with col1:
                st.markdown('<div class="form-container">', unsafe_allow_html=True)
                st.markdown("### 📊 Paramètres de Génération")
                
                # Sélection de la période
                col_a, col_b = st.columns(2)
                
                with col_a:
                    start_date = st.date_input("📅 Date de début", value=date(2025, 1, 1))
                
                with col_b:
                    end_date = st.date_input("📅 Date de fin", value=date(2025, 1, 31))
                
                # Sélection des enseignants
                if not enseignants_df.empty:
                    enseignants_options = [f"{row['Nom']} {row['Prénom']}" for _, row in enseignants_df.iterrows()]
                    selected_teachers = st.multiselect("👨‍🏫 Enseignants", enseignants_options, default=enseignants_options[0])
                    
                    if "Tous les enseignants" in selected_teachers:
                        teachers_to_process = enseignants_df.copy()
                    else:
                        teachers_to_process = enseignants_df[
                            enseignants_df.apply(lambda x: f"{x['Nom']} {x['Prénom']}" in selected_teachers, axis=1)
                        ]
                else:
                    st.warning("Aucun enseignant dans la base de données")
                    teachers_to_process = pd.DataFrame()
                
                # Options de calcul
                st.markdown("**💰 Paramètres de Calcul**")
                col_c, col_d = st.columns(2)
                
                with col_c:
                    prime_fixe = st.number_input("Prime fixe (FCFA)", min_value=0, value=0, step=5000)
                    prime_performance = st.checkbox("Prime de performance (+10%)")
                
                with col_d:
                    deduction_retard = st.number_input("Déduction retard (FCFA)", min_value=0, value=0, step=1000)
                    deduction_absence = st.number_input("Déduction absence (FCFA)", min_value=0, value=0, step=1000)
                
                # Options d'export
                st.markdown("**📄 Options d'Export**")
                col_e, col_f = st.columns(2)
                
                with col_e:
                    export_resume = st.checkbox("Résumé simple", value=True)
                    export_html = st.checkbox("Bulletins HTML professionnels", value=True)
                
                with col_f:
                    acompte_default = st.number_input("Acompte par défaut (FCFA)", min_value=0, value=0, step=1000)
                    montant_percu_auto = st.checkbox("Montant perçu = Montant net", value=True)
                
                # Génération
                if st.button("🔄 Générer les Fiches de Paie", type="primary", use_container_width=True):
                    if not teachers_to_process.empty and not seances_df.empty:
                        st.markdown("---")
                        st.markdown("### 📋 Fiches de Paie Générées")
                        
                        payroll_data = []
                        bulletins_html = {}  # Stockage des bulletins HTML
                        
                        for _, teacher in teachers_to_process.iterrows():
                            teacher_name = f"{teacher['Nom']} {teacher['Prénom']}"
                            teacher_nom = teacher['Nom']
                            teacher_ID = teacher['id']
                            teacher_statut = teacher['statut']

                            # Calcul des heures travaillées
                            hours_worked = calculate_worked_hours(seances_df, teacher_ID, start_date, end_date)
                            
                            # Récupération des séances pour ce prof dans la période
                            teacher_seances = get_teacher_sessions(seances_df, teacher_ID, start_date, end_date)
                            
                            # Calcul du salaire
                            taux_horaire = dict_honnoraire[teacher_statut]
                            salaire_base = taux_horaire * len(teacher_seances)
                            
                            # Calcul des primes
                            primes = prime_fixe
                            if prime_performance:
                                primes += int(salaire_base * 0.1)
                            
                            # Calcul des déductions (simplifiée)
                            deductions = deduction_retard + deduction_absence
                            
                            # Salaire net
                            salaire_net = int(salaire_base + primes - deductions)
                            
                            payroll_data.append({
                                "teacher_name": teacher_name,
                                "teacher_nom": teacher_nom,
                                "hours_worked": hours_worked,
                                "taux_horaire": taux_horaire,
                                "salaire_base": int(salaire_base),
                                "primes": primes,
                                "deductions": deductions,
                                "salaire_net": salaire_net,
                                "seances": teacher_seances
                            })
                            
                            # Génération du bulletin HTML professionnel
                            if export_html:
                                montant_percu = salaire_net if montant_percu_auto else None
                                bulletin_html = generer_bulletin_paie_html(
                                    nom_employe=teacher_nom,
                                    periode_debut=start_date.strftime('%d/%m/%Y'),
                                    periode_fin=end_date.strftime('%d/%m/%Y'),
                                    seances=teacher_seances,
                                    montant_a_payer=int(salaire_base),
                                    acompte=acompte_default,
                                    prime=primes,
                                    montant_percu=montant_percu
                                )
                                bulletins_html[teacher_name] = bulletin_html
                            
                            # Affichage du résumé (optionnel)
                            if export_resume:
                                st.markdown(f"""
                                <div class="payroll-card">
                                    <h4>👨‍🏫 {teacher_name}</h4>
                                    <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
                                        <div>
                                            <p><strong>⏱️ Heures travaillées:</strong> {hours_worked}h</p>
                                            <p><strong>📊 Séances effectuées:</strong> {len(teacher_seances)}</p>
                                            <p><strong>💰 Taux horaire:</strong> {taux_horaire:,} FCFA/ séance</p>
                                            <p><strong>📊 Salaire de base:</strong> {int(salaire_base):,} FCFA</p>
                                        </div>
                                        <div>
                                            <p><strong>🎁 Primes:</strong> {primes:,} FCFA</p>
                                            <p><strong>📉 Déductions:</strong> {deductions:,} FCFA</p>
                                            <p><strong>💵 SALAIRE NET:</strong> <span style="font-size: 1.2em; color: #28a745;">{salaire_net:,} FCFA</span></p>
                                        </div>
                                    </div>
                                    <p><strong>📅 Période:</strong> {start_date.strftime('%d/%m/%Y')} - {end_date.strftime('%d/%m/%Y')}</p>
                                </div>
                                """, unsafe_allow_html=True)
                        
                        # Affichage des bulletins HTML
                        if export_html and bulletins_html:
                            st.markdown("---")
                            st.markdown("### 📄 Bulletins de Paie Professionnels")
                            
                            # Sélecteur pour choisir quel bulletin afficher
                            selected_bulletin = st.selectbox(
                                "Choisir un bulletin à afficher :",
                                options=list(bulletins_html.keys()),
                                key="bulletin_selector"
                            )
                            
                            if selected_bulletin:
                                col_preview, col_download = st.columns([3, 1])
                                
                                with col_preview:
                                    # Aperçu du bulletin
                                    st.components.v1.html(bulletins_html[selected_bulletin], height=800, scrolling=True)
                                
                                with col_download:
                                    # Bouton de téléchargement individuel
                                    st.download_button(
                                        label=f"📥 Télécharger {selected_bulletin}",
                                        data=bulletins_html[selected_bulletin],
                                        file_name=f"bulletin_paie_{selected_bulletin.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.html",
                                        mime="text/html",
                                        use_container_width=True
                                    )
                            
                            # Option de téléchargement groupé
                            if len(bulletins_html) > 1:
                                st.markdown("#### 📦 Téléchargement groupé")
                                
                                # Création d'un archive ZIP (optionnel)
                                import zipfile
                                import io
                                
                                zip_buffer = io.BytesIO()
                                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                                    for teacher_name, bulletin_html in bulletins_html.items():
                                        filename = f"bulletin_paie_{teacher_name.replace(' ', '_')}_{start_date.strftime('%Y%m%d')}.html"
                                        zip_file.writestr(filename, bulletin_html)
                                
                                zip_buffer.seek(0)
                                
                                st.download_button(
                                    label="📦 Télécharger tous les bulletins (ZIP)",
                                    data=zip_buffer.getvalue(),
                                    file_name=f"bulletins_paie_{start_date.strftime('%Y%m%d')}_{end_date.strftime('%Y%m%d')}.zip",
                                    mime="application/zip",
                                    use_container_width=True
                                )
                        
                        # Sauvegarde dans Excel (votre code existant)
                        if payroll_data:
                            for pay in payroll_data:
                                #fiches_paie_df = read_from_supabase("Fiches_Paie")
                                id_fiche = len(fiches_paie_df) + 1
                                
                                data = [pay["teacher_name"],
                                    f"{start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}",
                                    pay["hours_worked"], pay["taux_horaire"], pay["salaire_base"],
                                    pay["primes"], pay["deductions"], pay["salaire_net"],
                                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                ]
                                
                                save_to_supabase("Fiches_Paie", data)
                                st.session_state.fiches_paie_df = read_from_supabase("Fiches_Paie")
                            
                            # Résumé total
                            total_net = sum(pay["salaire_net"] for pay in payroll_data)
                            total_hours = sum(pay["hours_worked"] for pay in payroll_data)
                            
                            st.markdown("---")
                            st.markdown(f"""
                            <div class="success-box">
                                <h4>📊 Résumé de la Paie</h4>
                                <p><strong>👥 Enseignants payés:</strong> {len(payroll_data)}</p>
                                <p><strong>⏱️ Total heures:</strong> {total_hours}h</p>
                                <p><strong>💰 Masse salariale:</strong> {total_net:,} FCFA</p>
                                <p><strong>📄 Bulletins générés:</strong> {len(bulletins_html) if export_html else 0}</p>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            
                    else:
                        st.warning("Aucune donnée disponible pour générer les fiches de paie")
                
                st.markdown('</div>', unsafe_allow_html=True)

            
            with col2:
                pass

        # ==================== ONGLET DES DONNES ====================
        with tab8:
            st.markdown("## 📊 Visualisation des Données")
            
            # Sélecteur de table à afficher
            table_choice = st.selectbox(
                "Choisir la table à afficher",
                ["Étudiants", "Dépenses", "Versements", "Ventes_Bords", "Présences"]
            )
            display_tab={"Étudiants":etudiants_df,"Dépenses":depenses_df,"Versements":versements_df,"Ventes_Bords":ventes_df,"Présences":presence_df}
            # Affichage des données
            #df_to_show = read_from_supabase(table_choice)
            df_to_show = display_tab.get(table_choice)

            if not df_to_show.empty:
                st.markdown(f"### 📋 Table: {table_choice}")
                st.markdown(f"**Nombre d'enregistrements:** {len(df_to_show)}")
                
                # Options d'affichage
                col1, col2 = st.columns([3, 1])
                
                with col2:
                    show_all = st.checkbox("Afficher toutes les colonnes", value=True)
                    max_rows = st.number_input("Nombre de lignes à afficher", min_value=5, max_value=1000, value=50)
                
                with col1:
                    if show_all:
                        st.dataframe(df_to_show.head(max_rows), use_container_width=True, hide_index=True)
                    else:
                        # Afficher seulement les premières colonnes importantes
                        cols_to_show = df_to_show.columns[:5]
                        st.dataframe(df_to_show[cols_to_show].head(max_rows), use_container_width=True, hide_index=True)

                # Bouton de téléchargement
                csv = df_to_show.to_csv(index=False)
                st.download_button(
                    label=f"📥 Télécharger {table_choice} en CSV",
                    data=csv,
                    file_name=f"{table_choice}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                    mime="text/csv"
                )
            else:
                st.info(f"Aucune donnée disponible dans la table {table_choice}")
            
            # Informations sur le fichier
            st.markdown("---")
            st.markdown("### 📁 Informations sur le fichier de données")
            
            if os.path.exists(EXCEL_FILE):
                file_size = os.path.getsize(EXCEL_FILE) / 1024  # en KB
                st.info(f"📊 Fichier: `{EXCEL_FILE}` | Taille: {file_size:.1f} KB")
            else:
                st.warning("Le fichier de données n'existe pas encore. Il sera créé lors du premier enregistrement.")
        #Enregistrement des données de connexion 
        data_connection=[user,'Administrateur', datetime.now().strftime('%Y-%m-%d %H:%M:%S')] 
        save_to_supabase("Connexion", data_connection)
if __name__ == "__main__":
    main()