import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title('Iris Species Classification')
st.write("The Iris dataset was used in R.A. Fisher's classic 1936 paper "
         "The Use of Multiple Measurements in Taxonomic Problems, "
         "and can also be found on the UCI Machine Learning Repository."
         "t includes three iris species with 50 samples each as well as some properties about each flower."
         "One flower species is linearly separable from the other two, "
         "but the other two are not linearly separable from each other."
         "The columns in this dataset are: "
         "-Id , SepalLengthCm , SepalWidthCm, PetalLengthCm, PetalWidthCm and species")

# penguin_file = st.file_uploader('Upload your own penguin data')
#
# if penguin_file is None:
#     rf_pickle = open('random_forest_penguin.pickle', 'rb')
#     map_pickle = open('output_penguin.pickle', 'rb')
#
#     rfc = pickle.load(rf_pickle)
#     unique_penguin_mapping = pickle.load(map_pickle)
#
#     rf_pickle.close()
# else:
#     penguin_df = pd.read_csv(penguin_file)
#     penguin_df = penguin_df.dropna()
#
#     output = penguin_df['species']
#     features = penguin_df[['island', 'bill_length_mm', 'bill_depth_mm',
#                            'flipper_length_mm', 'body_mass_g', 'sex']]
#
#     features = pd.get_dummies(features)
#
#     output, unique_penguin_mapping = pd.factorize(output)
#
#     x_train, x_test, y_train, y_test = train_test_split(
#         features, output, test_size=.8)
#
#     rfc = RandomForestClassifier(random_state=15)
#     rfc.fit(x_train, y_train)
#
#     y_pred = rfc.predict(x_test)
#
#     score = round(accuracy_score(y_pred, y_test), 2)
#
#     st.write('We trained a Random Forest model on these data,'
#              ' it has a score of {}! Use the '
#              'inputs below to try out the model.'.format(score))
#
# with st.form('user_inputs'):
#     island = st.selectbox('Penguin Island', options=[
#         'Biscoe', 'Dream', 'Torgerson'])
#     sex = st.selectbox('Sex', options=[
#         'Female', 'Male'])
#     bill_length = st.number_input(
#         'Bill Length (mm)', min_value=0, value=50)
#     bill_depth = st.number_input(
#         'Bill Depth (mm)', min_value=0, value=18)
#     flipper_length = st.number_input(
#         'Flipper Length (mm)', min_value=0, value=220)
#     body_mass = st.number_input(
#         'Body Mass (g)', min_value=0, value=3650)
#     st.form_submit_button()
#
# island_biscoe, island_dream, island_torgerson = 0, 0, 0
# if island == 'Biscoe':
#     island_biscoe = 1
# elif island == 'Dream':
#     island_dream = 1
# elif island == 'Torgerson':
#     island_torgerson = 1
#
# sex_female, sex_male = 0, 0
#
# if sex == 'Female':
#     sex_female = 1
#
# elif sex == 'Male':
#     sex_male = 1
#
# new_prediction = rfc.predict([[bill_length, bill_depth, flipper_length,
#                                body_mass, island_biscoe, island_dream,
#                                island_torgerson, sex_female, sex_male]])
# prediction_species = unique_penguin_mapping[new_prediction][0]
# st.write('We predict your penguin is of the {} species'.format(prediction_species))
