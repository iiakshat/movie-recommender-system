import streamlit as st
from pickle import load
import pandas as pd

st.title("Which Movie Should I Watch :red[Next]?")

data = load(open("movie_info.pkl", 'rb'))
similarity = load(open("similarity.pkl", 'rb'))

data2 = load(open("hollywood.pkl", 'rb'))
similarity2 = load(open("sim_hollywood.pkl", 'rb'))

movies = pd.DataFrame(data)
holly = pd.DataFrame(data2)

def recommended_movies(mov):
    try:
        idx = movies[movies["original_title"] == mov].index[0]
        corr = similarity[idx]
        rec = sorted(list(enumerate(corr)), reverse=True, key=lambda x: x[1])[1:6]

        l = []
        p = []
        c = []
        y = []

        for i in rec:
            p.append(movies.iloc[i[0]].poster_path)
            l.append(movies.iloc[i[0]].original_title)
            c.append(" ".join([movies.iloc[i[0]].genres][0]))
            y.append(movies.iloc[i[0]].year_of_release)
        return l,p,c,y
    except:
        l,p,c,y = recommended_holly(mov)
        return l,p,c,y

def recommended_holly(mov):
    idx = holly[holly["Title"] == mov].index[0]
    corr = similarity2[idx]
    rec = sorted(list(enumerate(corr)), reverse=True, key=lambda x: x[1])[1:11]

    l = []
    p = []
    c = []
    y = []

    for i in rec:
        p.append(holly.iloc[i[0]].Poster)
        l.append(holly.iloc[i[0]].Title)
        c.append(" ".join([holly.iloc[i[0]].Genre][0]))
        y.append(holly.iloc[i[0]].year)
    return l,p,c,y

choice = st.selectbox(
    'Enter Movie Name', holly['Title'].values
)

def details(mov):
    try:
        idx = movies[movies["original_title"] == mov].index[0]

        p = movies.iloc[idx].poster_path
        l = movies.iloc[idx].original_title
        c = " ".join([movies.iloc[idx].genres][0])
        y = movies.iloc[idx].year_of_release
        s = " ".join(movies.iloc[idx].summary)
        return l,p,c,y,s
    except:
        idx = holly[holly["Title"] == mov].index[0]
        p = holly.iloc[idx].Poster
        l = holly.iloc[idx].Title
        c = " ".join([holly.iloc[idx].Genre][0])
        y = holly.iloc[idx].year
        s = " "
        return l,p,c,y,s

    

if st.button("Recommend"):
    cola, colb, colc, cold, cole = st.columns(5)
    title, postr, cap, yr,story = details(choice)

    with colc:
        st.image(postr, width=220)
        st.header(title)
        st.subheader(f":blue[{yr}]")
        st.caption(f"Genre: {cap}")
        st.caption(story)


    st.header("More Like This :")
    title, postr, cap, yr = recommended_movies(choice)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(postr[0], width=115)
        st.subheader(title[0])
        st.subheader(f"   :blue[{yr[0]}]")
        st.caption(cap[0])
        # st.header("\n")
        # st.image(postr[5], width=115)
        # st.subheader(title[5])
        # st.subheader(f"   :blue[{yr[5]}]")
        # st.caption(cap[5])

    with col2:
        st.image(postr[1], width=115)
        st.subheader(title[1])
        st.subheader(f"   :blue[{yr[1]}]")
        st.caption(cap[1])
        # st.header("\n")
        # st.image(postr[6], width=115)
        # st.subheader(title[6])
        # st.subheader(f"   :blue[{yr[6]}]")
        # st.caption(cap[6])

    with col3:
        st.image(postr[2], width=115)
        st.subheader(title[2])
        st.subheader(f"   :blue[{yr[2]}]")
        st.caption(cap[2])
        # st.header("\n")
        # st.image(postr[7], width=115)
        # st.subheader(title[7])
        # st.subheader(f"   :blue[{yr[7]}]")
        # st.caption(cap[7])

    with col4:
        st.image(postr[3], width=115)
        st.subheader(title[3])
        st.subheader(f"   :blue[{yr[3]}]")
        st.caption(cap[3])
        # st.header("\n")
        # st.image(postr[8], width=115)
        # st.subheader(title[8])
        # st.subheader(f"   :blue[{yr[8]}]")
        # st.caption(cap[8])

    with col5:
        st.image(postr[4], width=115)
        st.subheader(title[4])
        st.subheader(f"   :blue[{yr[4]}]")
        st.caption(cap[4])
        # st.header("\n")
        # st.image(postr[9], width=115)
        # st.subheader(title[9])
        # st.subheader(f"   :blue[{yr[9]}]")
        # st.caption(cap[9])



if st.button("🌍"):
    cola, colb, colc, cold, cole = st.columns(5)
    title, postr, cap, yr,story = details(choice)

    with colc:
        st.image(postr, width=220)
        st.header(title)
        st.subheader(f":blue[{yr}]")
        st.caption(f"Genre: {cap}")
        st.caption(story)

    st.header("More Like This :")
    title, postr, cap, yr = recommended_holly(choice)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(postr[0], width=115)
        st.subheader(title[0])
        st.subheader(f"   :blue[{yr[0]}]")
        st.caption(cap[0])
        st.header("\n")
        st.image(postr[5], width=115)
        st.subheader(title[5])
        st.subheader(f"   :blue[{yr[5]}]")
        st.caption(cap[5])

    with col2:
        st.image(postr[1], width=115)
        st.subheader(title[1])
        st.subheader(f"   :blue[{yr[1]}]")
        st.caption(cap[1])
        st.header("\n")
        st.image(postr[6], width=115)
        st.subheader(title[6])
        st.subheader(f"   :blue[{yr[6]}]")
        st.caption(cap[6])

    with col3:
        st.image(postr[2], width=115)
        st.subheader(title[2])
        st.subheader(f"   :blue[{yr[2]}]")
        st.caption(cap[2])
        st.header("\n")
        st.image(postr[7], width=115)
        st.subheader(title[7])
        st.subheader(f"   :blue[{yr[7]}]")
        st.caption(cap[7])

    with col4:
        st.image(postr[3], width=115)
        st.subheader(title[3])
        st.subheader(f"   :blue[{yr[3]}]")
        st.caption(cap[3])
        st.header("\n")
        st.image(postr[8], width=115)
        st.subheader(title[8])
        st.subheader(f"   :blue[{yr[8]}]")
        st.caption(cap[8])

    with col5:
        st.image(postr[4], width=115)
        st.subheader(title[4])
        st.subheader(f"   :blue[{yr[4]}]")
        st.caption(cap[4])
        st.header("\n")
        st.image(postr[9], width=115)
        st.subheader(title[9])
        st.subheader(f"   :blue[{yr[9]}]")
        st.caption(cap[9])




# Adding Tick-Box Feature :

    # agree = st.checkbox('Show Hollywood')
    # if agree:
    #     title, postr, cap, yr = recommended_holly(choice)
    #     with col1:
    #         st.image(postr[0], width=115)
    #         st.subheader(title[0])
    #         st.subheader(f"   :blue[{yr[0]}]")
    #         st.caption(cap[0])

    #     with col2:
    #         st.image(postr[1], width=115)
    #         st.subheader(title[1])
    #         st.subheader(f"   :blue[{yr[1]}]")
    #         st.caption(cap[1])

    #     with col3:
    #         st.image(postr[2], width=115)
    #         st.subheader(title[2])
    #         st.subheader(f"   :blue[{yr[2]}]")
    #         st.caption(cap[2])

    #     with col4:
    #         st.image(postr[3], width=115)
    #         st.subheader(title[3])
    #         st.subheader(f"   :blue[{yr[3]}]")
    #         st.caption(cap[3])

    #     with col5:
    #         st.image(postr[4], width=115)
    #         st.subheader(title[4])
    #         st.subheader(f"   :blue[{yr[4]}]")
    #         st.caption(cap[4])