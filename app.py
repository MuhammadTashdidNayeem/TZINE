import streamlit as st
st.title('              :green[TZINE]')
st.image('new.png')
st.write("Welcome to TZINE, your one-stop destination for high-quality design services. As a skilled graphic and t-shirt designer, I offer a range of design services to help businesses and individuals bring their ideas to life. With a focus on simplicity and creativity, I strive to deliver designs that are both beautiful and functional, tailored to meet the unique needs of each client. From logo design to custom apparel, I am committed to providing top-notch design services that exceed your expectations. Collaborate with me today and let's make something amazing together!")
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Flyer", "Brochure", "T-Shirt", "Banner","Business Card","Book Cover","Package","Photography"])
with tab1:
    st.header(":green[Flyer TZINE]")  
    st.image("f1.png")
    st.image("f2.png")
    st.image("f3.png")  
with tab2:
    st.header(":green[Brochure TZINE]")
    st.image("b1.png")
    st.image("b2.png")   
with tab3:
    st.header(":green[T-Shirt TZINE]")
    st.image("t1.png")
    st.image('t2.jpg')    
with tab4:
    st.header(":green[Banner TZINE]")
    st.image("b3.png")
    st.image("b4.png")
with tab5:
    st.header(":green[Business Card TZINE]")
    st.image("c1.jpg")    
with tab6:
    st.header(":green[Book Cover TZINE]")
    st.image("bo.png")
with tab7:
    st.header(":green[Package TZINE]")
    st.image("p.png") 
with tab8:    
    st.header(':green[My Photography]')
    st.image('p2.jpg', caption='Cycnonotidie')
    st.image('p1.jpg', caption='The Sunset')
    st.image('p3.jpg', caption='The Insect')
    st.image('p4.jpg', caption='The Crow')
    st.image('p5.jpg', caption="Beehive")
    st.image('p6.jpg', caption='Pigeons')
st.header(":green[Hire ME]") 
option = st.selectbox(
    '',
    ('Part Time- Graphics TZINE', 'Full Time- Graphics TZINE', 'Part Time- T-Shirt TZINE ', 'Full Time T-Shirt TZINE', 'Photography'))


st.write('You selected:', option, )
if st.button('Submit'):
    st.write('Make a Screenshot and send it to tzine@gmail.com')
st.header(":green[For any query]")
st.write('Email-tzine@gmail.com')