import streamlit as st
from Fonction import *


# Configuration de la page
st.set_page_config(
    page_title="Centre de Préparation aux Examens",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

#boutton de mise à jour
refresh=st.sidebar.button("Actualiser")
if refresh:
    etudiants_df, enseignants_df, seances_df, depenses_df, versements_df, ventes_df, presence_df, presences_df, fiches_paie_df, statut_df, Connect_df=load_all_data()

    photo=st.sidebar.camera_input("Prendre une photo")
    st.rerun()


etudiants_df, enseignants_df, seances_df, depenses_df, versements_df, ventes_df, presence_df, presences_df, fiches_paie_df, statut_df, Connect_df=load_all_data()

#etudiants_df["DateArrivée"]=pd.to_datetime(etudiants_df['DateArrivée']).dt.date
#etudiants_df['DateArrivée'] = etudiants_df['DateArrivée'].dt.strftime('%Y-%m-%d')

#versements_df["Date"]=pd.to_datetime(versements_df['Date']).dt.date
#versements_df['Date'] = versements_df['Date'].dt.strftime('%Y-%m-%d')

#depenses_df["Date"]=pd.to_datetime(depenses_df['Date']).dt.date
#depenses_df['Date'] = depenses_df['Date'].dt.strftime('%Y-%m-%d')
#etudiants_df
versements_df["Montant"]=versements_df["Montant"].astype(int)

# CSS personnalisé pour un design moderne
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
    }
    
    .concours-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #2a5298;
    }
    
    .stat-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 1rem;
    }
    
    .info-section {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    
    .center-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .chat-message-user {
        background: #e3f2fd;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        margin-left: 2rem;
        border-left: 4px solid #2196f3;
    }
    
    .chat-message-assistant {
        background: #f3e5f5;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        margin-right: 2rem;
        border-left: 4px solid #9c27b0;
    }
    
    .chat-container {
        max-height: 400px;
        overflow-y: auto;
        padding: 1rem;
        background: white;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Base de connaissances du chatbot
KNOWLEDGE_BASE = {
    "concours": {
        "ISE LONG / AS": {
            "nom_complet": "Ingénieur Statisticien Économiste - Cycle Long",
            "duree": "6 mois de préparation intensive",
            "matieres": ["Mathématiques", "Statistiques", "Économie", "Anglais"],
            "niveau": "Bac+5",
            "debouches": "Postes d'ingénieurs dans les instituts de statistique"
        },
        "ISE ECO": {
            "nom_complet": "Ingénieur Statisticien Économiste - Économie",
            "duree": "4 mois de préparation",
            "matieres": ["Économie", "Mathématiques", "Comptabilité", "Anglais"],
            "niveau": "Bac+5",
            "debouches": "Postes d'économistes et analystes"
        },
        "ISE MATH": {
            "nom_complet": "Ingénieur Statisticien Économiste - Mathématiques",
            "duree": "5 mois de préparation",
            "matieres": ["Mathématiques avancées", "Logique", "Statistiques", "Informatique"],
            "niveau": "Bac+5",
            "debouches": "Postes de mathématiciens et statisticiens"
        },
        "IFORD A": {
            "nom_complet": "Institut de Formation et de Recherche Démographiques - Niveau A",
            "duree": "3 mois de préparation",
            "matieres": ["Démographie", "Statistiques", "Économie", "Géographie"],
            "niveau": "Bac+3",
            "debouches": "Postes de démographes et analystes"
        },
        "IFORD B": {
            "nom_complet": "Institut de Formation et de Recherche Démographiques - Niveau B",
            "duree": "4 mois de préparation",
            "matieres": ["Sciences sociales", "Statistiques", "Informatique", "Démographie"],
            "niveau": "Bac+2",
            "debouches": "Postes de techniciens en démographie"
        },
        "TSS": {
            "nom_complet": "Technicien Supérieur de la Statistique",
            "duree": "5 mois de préparation",
            "matieres": ["Statistiques", "Mathématiques", "Informatique", "Économie"],
            "niveau": "Bac+2",
            "debouches": "Postes de techniciens statisticiens"
        }
    },
    "centres": {
        "Yaoundé": {
            "adresse": "Centre ville, Yaoundé",
            "telephone": "+237 6XX XXX XXX",
            "horaires": "Lun-Ven: 15h30-18h30, Sam: 11h00-16h00, Dim: 10h00-13h00"
        },
        "Douala": {
            "adresse": "Akwa, Douala",
            "telephone": "+237 6XX XXX XXX",
            "horaires": "Lun-Ven: 15h30-18h30, Sam: 11h00-16h00, Dim: 10h00-13h00"
        },
        "Dschang": {
            "adresse": "Campus universitaire, Dschang",
            "telephone": "+237 6XX XXX XXX",
            "horaires": "Lun-Ven: 15h30-18h30, Sam: 11h00-16h00, Dim: 10h00-13h00"
        }
    },
    "infos_generales": {
        "taux_reussite": "85%",
        "nombre_etudiants": "500+",
        "email": "info@centrepreparation.cm",
        "documents_requis": ["Copie CNI", "Diplôme/relevé de notes", "2 photos d'identité", "Frais d'inscription"],
        "services": ["Cours magistraux", "Travaux dirigés", "Concours blancs", "Suivi personnalisé", "Documentation complète"],
        "paiement": ["Comptant", "Échelonné", "Mobile Money", "Virement bancaire"]
    }
}

def get_chatbot_response(user_message):
    """Génère une réponse du chatbot basée sur le message de l'utilisateur"""
    message_lower = user_message.lower()
    
    # Salutations
    if any(word in message_lower for word in ["bonjour", "salut", "hello", "bonsoir"]):
        return "👋 Bonjour ! Je suis ravi de vous aider. Que souhaitez-vous savoir sur STATO-SPHERE PREPAS ?"
    
    # Questions sur les concours
    for concours, details in KNOWLEDGE_BASE["concours"].items():
        if any(word in message_lower for word in concours.lower().split()):
            return f"""📚 **{concours}** - {details['nom_complet']}
            
**Durée de préparation :** {details['duree']}
**Niveau requis :** {details['niveau']}
**Matières principales :** {', '.join(details['matieres'])}
**Débouchés :** {details['debouches']}

Souhaitez-vous plus d'informations sur ce concours ou sur nos modalités d'inscription ?"""
    
    # Questions générales sur les concours
    if any(word in message_lower for word in ["concours", "préparation", "examen"]):
        return """📚 **Nos concours préparés :**
        
• ISE LONG / AS - Ingénieur Statisticien Économiste Cycle Long
• ISE ECO - Ingénieur Statisticien Économiste Économie  
• ISE MATH - Ingénieur Statisticien Économiste Mathématiques
• IFORD A - Institut de Formation Démographique Niveau A
• IFORD B - Institut de Formation Démographique Niveau B
• TSS - Technicien Supérieur de la Statistique

Quel concours vous intéresse ? Je peux vous donner plus de détails !"""
    
    # Questions sur les centres
    if any(word in message_lower for word in ["centre", "adresse", "localisation", "où"]):
        return """📍 **Nos centres :**
        
**Yaoundé** - Centre ville
📞 +237 6XX XXX XXX

**Douala** - Akwa  
📞 +237 6XX XXX XXX

**Dschang** - Campus universitaire
📞 +237 6XX XXX XXX

**Horaires :** Lun-Ven 15h30-18h30, Sam 11h00-16h00, Dim 10h00-13h00"""
    
    # Questions sur les tarifs
    if any(word in message_lower for word in ["prix", "tarif", "coût", "payer", "paiement"]):
        return """💰 **Modalités de paiement :**
        
• Paiement comptant
• Paiement échelonné  
• Mobile Money
• Virement bancaire

Pour connaître les tarifs exacts, contactez-nous au +237 6XX XXX XXX ou visitez l'un de nos centres."""
    
    # Questions sur les horaires
    if any(word in message_lower for word in ["horaire", "heure", "ouvert", "fermé"]):
        return """⏰ **Nos horaires :**
        
**Lundi - Vendredi :** 15h30 - 18h30
**Samedi :** 11h00 - 16h00  
**Dimanche :** 10h00 - 13h00

Tous nos centres suivent ces horaires."""
    
    # Questions sur l'inscription
    if any(word in message_lower for word in ["inscription", "inscrire", "document", "s'inscrire"]):
        return """📋 **Pour vous inscrire :**
        
**Documents requis :**
• Copie de la CNI
• Diplôme ou relevé de notes
• 2 photos d'identité  
• Frais d'inscription

**Démarche :** Rendez-vous dans l'un de nos centres avec ces documents.
**Contact :** +237 6XX XXX XXX ou info@centrepreparation.cm"""
    
    # Questions sur les résultats
    if any(word in message_lower for word in ["résultat", "taux", "réussite", "statistique"]):
        return f"""🏆 **Nos résultats :**
        
• **Taux de réussite 2024 :** {KNOWLEDGE_BASE['infos_generales']['taux_reussite']}
• **Étudiants formés :** {KNOWLEDGE_BASE['infos_generales']['nombre_etudiants']}
• **3 centres actifs** à Yaoundé, Douala et Dschang

Notre méthode éprouvée garantit votre réussite !"""
    
    # Questions sur les services
    if any(word in message_lower for word in ["service", "cours", "offre", "formation"]):
        return """🎯 **Nos services :**
        
• Cours magistraux par des experts
• Travaux dirigés personnalisés
• Concours blancs réguliers  
• Suivi personnalisé de chaque étudiant
• Documentation complète et actualisée
• Coaching et motivation

Une approche complète pour votre réussite !"""
    
    # Contact
    if any(word in message_lower for word in ["contact", "téléphone", "email", "joindre"]):
        return """📞 **Nous contacter :**
        
**📧 Email :** info@centrepreparation.cm
**📱 Téléphone :** +237 6XX XXX XXX
**💬 WhatsApp :** +237 6XX XXX XXX
**📘 Facebook :** CentrePreparationCM

N'hésitez pas à nous contacter pour toute question !"""
    
    # Au revoir
    if any(word in message_lower for word in ["au revoir", "bye", "merci", "à bientôt"]):
        return "👋 Merci de votre visite ! N'hésitez pas à revenir si vous avez d'autres questions. Bonne chance pour vos préparations ! 🎓"
    
    # Réponse par défaut
    return """🤔 Je ne suis pas sûr de comprendre votre question. 

**Je peux vous renseigner sur :**
• Nos concours (ISE, IFORD, TSS)
• Nos centres (Yaoundé, Douala, Dschang)  
• Les modalités d'inscription
• Les horaires et tarifs
• Nos services et résultats

Que souhaitez-vous savoir ?"""

def main():
    # En-tête principal
    st.markdown("""
    <div class="main-header">
        <h1>🎓 Centre de Préparation aux Examens</h1>
        <h3>Excellence • Formation • Réussite</h3>
        <p>Votre partenaire de confiance pour la réussite aux concours</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Depliant sur les informations du concours")
    #show_pdf("MATH.pdf")
    fichier="MATH.pdf"
    if st.button("Ouvrir le depliant",key="sdknckd"):
        show_pdf("MATH.pdf")
    
    # Section actualités/annonces
    st.markdown("## 📢 Actualités et Annonces")
    col1, col2 = st.columns([2, 1])
    
    
    with col1:
        st.info("🔥 **Nouvelle session 2025** - Les inscriptions sont ouvertes pour tous les concours !")
        st.success("✅ **Taux de réussite 2024** - 85% de nos étudiants ont réussi leurs concours")
        
    with col2:
        st.markdown("""
        <div class="stat-box">
            <h3>🏆 Statistiques 2024</h3>
            <p><strong>500+</strong> Étudiants formés</p>
            <p><strong>85%</strong> Taux de réussite</p>
            <p><strong>3</strong> Centres actifs</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Section concours disponibles
    st.markdown("## 📚 Concours Préparés")
    
    # Données des concours
    concours_data = {
        "ISE LONG / AS": {
            "description": "Institut Supérieur d'Enseignement - Cycle Long / Assistant Sanitaire",
            "duree": "Préparation intensive de 6 mois",
            "matiere": "Sciences médicales, Biologie, Chimie",
            "places": "Places limitées disponibles"
        },
        "ISE ECO": {
            "description": "Institut Supérieur d'Enseignement - Économie",
            "duree": "Préparation de 4 mois",
            "matiere": "Économie, Mathématiques, Comptabilité",
            "places": "Inscription ouverte"
        },
        "ISE MATH": {
            "description": "Institut Supérieur d'Enseignement - Mathématiques",
            "duree": "Préparation de 5 mois",
            "matiere": "Mathématiques avancées, Logique, Statistiques",
            "places": "Inscription ouverte"
        },
        "IFORD A": {
            "description": "Institut de Formation et de Recherche Démographiques - Niveau A",
            "duree": "Préparation de 3 mois",
            "matiere": "Démographie, Statistiques, Économie",
            "places": "Dernières places"
        },
        "IFORD B": {
            "description": "Institut de Formation et de Recherche Démographiques - Niveau B",
            "duree": "Préparation de 4 mois",
            "matiere": "Sciences sociales, Statistiques, Informatique",
            "places": "Inscription ouverte"
        },
        "TSS": {
            "description": "Technicien Supérieur de la Statistique",
            "duree": "Préparation de 5 mois",
            "matiere": "Statistiques, Mathématiques, Informatique",
            "places": "Places disponibles"
        }
    }
    
    # Affichage des concours en colonnes
    col1, col2 = st.columns(2)
    
    for i, (concours, details) in enumerate(concours_data.items()):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="concours-card">
                <h4>🎯 {concours}</h4>
                <p><strong>Description:</strong> {details['description']}</p>
                <p><strong>Durée:</strong> {details['duree']}</p>
                <p><strong>Matières:</strong> {details['matiere']}</p>
                <p><strong>Statut:</strong> <span style="color: #28a745; font-weight: bold;">{details['places']}</span></p>
            </div>
            """, unsafe_allow_html=True)
    
    # Section centres
    st.markdown("## 🏢 Nos Centres")
    
    col1, col2, col3 = st.columns(3)
    
    centres = [
        {"nom": "Yaoundé", "adresse": "Centre ville", "tel": "+237 6XX XXX XXX"},
        {"nom": "Douala", "adresse": "Akwa", "tel": "+237 6XX XXX XXX"},
        {"nom": "Dschang", "adresse": "Campus universitaire", "tel": "+237 6XX XXX XXX"}
    ]
    
    for i, centre in enumerate(centres):
        with [col1, col2, col3][i]:
            st.markdown(f"""
            <div class="center-card">
                <h4>📍 {centre['nom']}</h4>
                <p><strong>Adresse:</strong> {centre['adresse']}</p>
                <p><strong>Téléphone:</strong> {centre['tel']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Section informations pratiques
    st.markdown("## ℹ️ Informations Pratiques")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-section">
            <h4>⏰ Horaires</h4>
            <ul>
                <li><strong>Lundi - Vendredi:</strong> 8h00 - 18h00</li>
                <li><strong>Samedi:</strong> 8h00 - 14h00</li>
                <li><strong>Dimanche:</strong> Fermé</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-section">
            <h4>📋 Documents requis</h4>
            <ul>
                <li>Copie de la CNI</li>
                <li>Diplôme ou relevé de notes</li>
                <li>2 photos d'identité</li>
                <li>Frais d'inscription</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-section">
            <h4>🎯 Nos Services</h4>
            <ul>
                <li>Cours magistraux</li>
                <li>Travaux dirigés</li>
                <li>Concours blancs</li>
                <li>Suivi personnalisé</li>
                <li>Documentation complète</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="info-section">
            <h4>💰 Modalités de paiement</h4>
            <ul>
                <li>Paiement comptant</li>
                <li>Paiement échelonné</li>
                <li>Mobile Money</li>
                <li>Virement bancaire</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Section Chatbot intégré
    if "messages" not in st.session_state:
        st.session_state.messages = [
        {"role": "assistant", "content": "👋 Bonjour ! Je suis l'assistant virtuel de STATO-SPHERE PREPAS. Comment puis-je vous aider aujourd'hui ? Vous pouvez me poser des questions sur nos concours, nos centres, les modalités d'inscription, etc."}
    ]
    st.markdown("## 🤖 Assistant Virtuel - Posez vos questions !")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Container pour le chat
        st.markdown("""
        <div style="background: #f8f9fa; padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
            <h4>💬 Chattez avec notre assistant intelligent</h4>
            <p>Notre assistant peut répondre à toutes vos questions sur les concours, les centres, les inscriptions, etc.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Affichage des messages du chat
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        if len(st.session_state.messages) > 1:  # Plus que le message d'accueil
            for message in st.session_state.messages:
                if message["role"] == "user":
                    st.markdown(f"""
                    <div class="chat-message-user">
                        <strong>👤 Vous :</strong> {message["content"]}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="chat-message-assistant">
                        <strong>🤖 Assistant :</strong><br>{message["content"]}
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message-assistant">
                <strong>🤖 Assistant :</strong><br>{st.session_state.messages[0]["content"]}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Input pour nouveau message
        user_input = st.text_input("💬 Tapez votre message ici...", key="chat_input", placeholder="Ex: Quels concours préparez-vous ?")
        
        # Boutons de suggestions rapides
        st.markdown("**🚀 Questions rapides :**")
        col_q1, col_q2, col_q3 = st.columns(3)
        
        with col_q1:
            if st.button("📚 Nos concours", key="q1"):
                st.session_state.messages.append({"role": "user", "content": "Quels concours préparez-vous ?"})
                response = get_chatbot_response("Quels concours préparez-vous ?")
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
        
        with col_q2:
            if st.button("📍 Nos centres", key="q2"):
                st.session_state.messages.append({"role": "user", "content": "Où sont situés vos centres ?"})
                response = get_chatbot_response("Où sont situés vos centres ?")
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
        
        with col_q3:
            if st.button("📋 Inscription", key="q3"):
                st.session_state.messages.append({"role": "user", "content": "Comment puis-je m'inscrire ?"})
                response = get_chatbot_response("Comment puis-je m'inscrire ?")
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
        
        col_q4, col_q5, col_q6 = st.columns(3)
        
        with col_q4:
            if st.button("💰 Tarifs", key="q4"):
                st.session_state.messages.append({"role": "user", "content": "Quels sont vos tarifs ?"})
                response = get_chatbot_response("Quels sont vos tarifs ?")
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
        
        with col_q5:
            if st.button("🏆 Résultats", key="q5"):
                st.session_state.messages.append({"role": "user", "content": "Quels sont vos résultats ?"})
                response = get_chatbot_response("Quels sont vos résultats ?")
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
        
        with col_q6:
            if st.button("📞 Contact", key="q6"):
                st.session_state.messages.append({"role": "user", "content": "Comment vous contacter ?"})
                response = get_chatbot_response("Comment vous contacter ?")
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
        
        col_send, col_clear = st.columns([1, 1])
        with col_send:
            if st.button("📤 Envoyer", type="primary", use_container_width=True):
                if user_input:
                    # Ajouter le message de l'utilisateur
                    st.session_state.messages.append({"role": "user", "content": user_input})
                    
                    # Générer et ajouter la réponse du chatbot
                    response = get_chatbot_response(user_input)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    
                    # Rerun pour afficher les nouveaux messages
                    st.rerun()
        
        with col_clear:
            if st.button("🗑️ Nouveau chat", use_container_width=True):
                st.session_state.messages = [
                    {"role": "assistant", "content": "👋 Bonjour ! Je suis l'assistant virtuel de STATO-SPHERE PREPAS. Comment puis-je vous aider aujourd'hui ? Vous pouvez me poser des questions sur nos concours, nos centres, les modalités d'inscription, etc."}
                ]
                st.rerun()
    
    with col2:
        st.markdown("""
        <div style="background: #e8f5e8; padding: 1rem; border-radius: 10px; margin-bottom: 1rem;">
            <h4>💡 Conseils d'utilisation</h4>
            <p><strong>Vous pouvez demander :</strong></p>
            <ul>
                <li>Informations sur les concours</li>
                <li>Localisation des centres</li>
                <li>Procédures d'inscription</li>
                <li>Tarifs et modalités</li>
                <li>Taux de réussite</li>
                <li>Documents requis</li>
                <li>Horaires d'ouverture</li>
                <li>Coordonnées de contact</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: #fff3e0; padding: 1rem; border-radius: 10px;">
            <h4>🎯 Astuce</h4>
            <p>Utilisez les <strong>boutons rapides</strong> ci-contre pour poser les questions les plus fréquentes en un clic !</p>
            <p>Notre assistant répond instantanément à vos questions sur STATO-SPHERE PREPAS.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Section contact
    st.markdown("## 📞 Contact")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **📧 Email**  
        info@centrepreparation.cm  
        contact@centrepreparation.cm
        """)
    
    with col2:
        st.markdown("""
        **📱 Téléphones**  
        +237 6XX XXX XXX  
        +237 6XX XXX XXX
        """)
    
    with col3:
        st.markdown("""
        **🌐 Réseaux sociaux**  
        Facebook: CentrePreparationCM  
        WhatsApp: +237 6XX XXX XXX
        """)
    
    # Pied de page
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        <p>© 2025 Centre de Préparation aux Examens - Tous droits réservés</p>
        <p>🎓 Excellence • Formation • Réussite</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()