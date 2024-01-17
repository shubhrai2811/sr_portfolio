from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
data = {}


def index(request):
    global data

    # Change your name and description here
    data["yourname"] = "Shubh Rai"
    data["whatareyou"] = ["Gaming","Programming","Data Science","Exploring","Travelling"]

    # about
    data[
        "aboutpara1"
    ] = " I'm Shubh, a pre-final year B.Tech in Computer Science at Indian Institute of Information Technology Kalyani (IIITK). I'm not your average engineer; I'm a tinkerer, a puzzle solver, maker of things. My interests and skills extend to Machine Learning, Data Science, Mobile apps development and System Design, From crafting mobile apps that dance in your pocket to building brainboxes that learn like lightning, I'm all about using tech to make the world a bit cooler, one line of code at a time."
    data[
        "aboutpara2"
    ] = "I like to work with new tools and technologies,I’m always down for hearing about new projects, so feel free to drop me a text on any of my social media. "
    data["aboutimage"] = "image/Shubh.jpeg"

    # my journey (can have max 4 only)
    data["journey1"] = {
        "startyear": "2021",
        "endyear": "",
        "desc": "Started my B.Tech CSE at IIIT Kalyani, West-Bengal",
    }
    data["journey2"] = {
        "startyear": "2022",
        "endyear": "",
        "desc": "Winner at Smart India Hackathon 2022",
    }
    data["journey3"] = {
        "startyear": "2023",
        "endyear": "",
        "desc": "Amazon ML Summer School, Finalist at Smart India Hackathon 2023",
    }
    data["journey4"] = {
        "startyear": "2024",
        "endyear": "",
        "desc": "Looking for Job/Internship Opportunities while upskilling",
    }

    # my skills
    data["skills"] = [
        {"name": "C++", "icon": "icons/kevalvavaliya-cpp.svg"},
        {"name": "Python", "icon": "icons/kevalvavaliya-python.svg"},
        {"name": "Android", "icon": "icons/kevalvavaliya-android.svg"},
        {"name": "Dart", "icon": "icons/kevalvavaliya-dart.svg"},
        {"name": "Flutter", "icon": "icons/kevalvavaliya-flutter.svg"},
        {"name": "Django", "icon": "icons/kevalvavaliya-django.svg"},
        {"name": "JavaScript", "icon": "icons/kevalvavaliya-js.svg"},
        {"name": "Tensorflow", "icon": "icons/kevalvavaliya-tensorflow.svg"},
        {"name": "Linux", "icon": "icons/kevalvavaliya-lin.svg"},
        {"name": "Firebase", "icon": "icons/kevalvavaliya-firebase.svg"},
        {"name": "Docker", "icon": "icons/kevalvavaliya-docker.svg"},
        {"name": "MySQL", "icon": "icons/kevalvavaliya-mysql.svg"},
        {"name": "Github", "icon": "icons/kevalvavaliya-github.svg"},
        {"name": "Matlab", "icon": "icons/matlab.svg"},
        {"name": "Google Cloud", "icon": "icons/kevalvavaliya-googlecloud.svg"},
        {"name": "Flask", "icon": "icons/kevalvavaliya-flask.svg"},
        {"name": "HTML", "icon": "icons/kevalvavaliya-html.svg"},
        {"name": "CSS", "icon": "icons/kevalvavaliya-css.svg"},
        {"name": "PHP", "icon": "icons/kevalvavaliya-php.svg"},
        # {"name": "JQuery", "icon": "icons/kevalvavaliya-jquery.svg"},
        
        
        
        # {"name": "Wordpress", "icon": "icons/kevalvavaliya-wordpress.svg"},
        
        
        
        {"name": "PostgreSQL", "icon": "icons/kevalvavaliya-postgresql.svg"},
        {"name": "CockroachDB", "icon": "icons/cockroachdb.svg"},
        
        
    ]

    # social-links
    data["social_links"] = [
        {"name": "Github", "socialURL": "https://github.com/shubhrai2811"},
        {"name": "Twitter", "socialURL": "https://twitter.com/blackJaguar__"},
        {"name": "Linkedin", "socialURL": "https://www.linkedin.com/in/2811shubh/"},
        {"name": "Instagram", "socialURL": "https://www.instagram.com/battery_saving_mode/"},
    ]

    # projects
    data["projects"] = [
        {
            "id": "01",
            "name": "Signal Sensei: FEC Identification - SIH2023 Finalist",
            "github": "https://github.com/FEC-SIH-23/Blind-FEC-Extractor",
            "projectimg": "image/project/fec.png",
            "tech": "ML, Deep Learning, RNN, Data Generation, Signal Processing",
            "finalist":"Smart India Hackathon 2023",
            "desc": "Unleashing the Power of Artificial Intelligence, One Algorithm at a Time: Blind-FEC-Extractor disrupts the boundaries of signal processing, demonstrating the remarkable capabilities of AI to uncover hidden structures within the most complex signals."

,
        },
        {
            "id": "02",
            "name": "LipSeer: Seeing Words Through Lips",
            "github": "https://github.com/shubhrai2811/LipBuddy",
            "Kaggle Notebook":"https://www.kaggle.com/code/prolevelnoob/shubh-lipreader",
            "projectimg": "image/project/lips.png",
            "tech": "ML, Neural Network, Streamlit, OpenCV, Django",
            "desc": " When words can't be heard, LipBuddy will listen. Unlocking communication beyond sound, empowering understanding through the power of visual speech recognition.",
        },
        {
            "id": "03",
            "name": "FutureValuEstate - Status Code 0 Hackathon Finalist",
            "github": "https://github.com/shubhrai2811/JAPAN-Real-Estate-Valuation",
            "live": "https://jp-real-estate-valuation.streamlit.app/",
            "projectimg": "image/project/fve.png",
            "tech": "Streamlit, CNN, ML, Django",
            "finalist":"Status Code 0 Hackathon",
            "desc": "Peer into the crystal ball of real estate with a single click. FutureValuEstate: Empowering informed decisions and strategic investments through cutting-edge AI forecasting.",
        },
        {
            "id": "04",
            "name": "AirComms - SIH2022 Winner",
            "github": "https://github.com/shubhrai2811/SIH-2022-Fourier-Encoder-Decoder",
            "projectimg": "image/project/fourier.png",
            "tech": "C++, Python, ML, Image Processing",
            "winner":"Smart India Hackathon 2022",
            "desc": "Walkie-talkies meet multimedia: See what they see, hear what they hear. Fourier Encoder-Decoder unlocks a new era of police communication, transforming ordinary radio sets into powerful multimedia conduits.",
        },
        {
            "id": "05",
            "name": "Not-MineCraft",
            "github": "https://github.com/shubhrai2811/NotMineCraft.github.io/tree/main/projects/shubh/Not%20Minecraft",
            "projectimg": "image/project/nmc.png",
            "tech": "JS, ReactJS, ThreeJS, Game Development, HTML",
            "winner":"JS Bootcamp IIITK",
            "desc": "Craft your adventure, anywhere, anytime: No downloads, no limits. Infinite worlds of blocky joy, optimized for your browser, ready to spark your creativity, right at your fingertips. Minecraft, reimagined for the web.",
        },
        # {
        #     "id": "06",
        #     "name": "Goverdhan Institute site",
        #     "github": "https://github.com/kevalvavaliya/Goverdhan-infotech",
        #     "projectimg": "image/project/kevalvavaliya-goverdhan.png",
        #     "tech": "#DJANGO #HTML #CSS #JS #MYSQL",
        #     "desc": "Education site for goverdhan institute that manages the courses and events online which makes student easy to reach them.",
        # },
        # {
        #     "id": "07",
        #     "name": "We-Donate",
        #     "github": "https://github.com/kevalvavaliya/We-Donate",
        #     "projectimg": "image/project/kevalvavaliya-wedonate.png",
        #     "tech": "#ANDROID #FLASK #XML #COCKROACHDB #JAVA",
        #     "desc": "We-Donate aims in bringing digitization in donation.we donate delivers your donation to the right hands and provides home pickup services.",
        # },
        # {
        #     "id": "08",
        #     "name": "Localens",
        #     "github": "https://github.com/kevalvavaliya/Localens",
        #     "projectimg": "image/project/kevalvavaliya-localens.png",
        #     "tech": "#ANDROID #FLASK #XML #COCKROACHDB #JAVA",
        #     "desc": "Localens is an android app for finding local beauty spots in your localities and get them capture in the app and take it to the world",
        # },
        # {
        #     "id": "09",
        #     "name": "Vishvas Fabrics Ecommerce site",
        #     "github": "https://github.com/kevalvavaliya/E-commerce-site",
        #     "projectimg": "image/project/kevalvavaliya-vishvas.png",
        #     "tech": "#PHP #HTML #CSS #JS #MYSQL",
        #     "desc": "A basic ecommerce site for vishvas fabrics",
        # },
        # {
        #     "id": "10",
        #     "name": "Sachivato news and blog site",
        #     "projectimg": "image/project/itemcover.png",
        #     "tech": "#WORDPRESS #DIGITALOCEAN",
        #     "desc": "A basic News and Blog wordpress site",
        # },
    ]
    data[
        "resumelink"
    ]= "https://drive.google.com/file/d/1kBTlV-u-1XhT8G9a-xmEJ4XlNUeNPBdb/view?usp=sharing"

    return render(request, "index.html", data)
