// HomePage.js
import React from 'react';
import Menu from './Menu';
import ImageSlideShow from './component/ImageSlideShow';
import ExerciseGrid from './component/excercise_grid';
import Footer from './component/footer';
import TrainingProgram from './component/TrainingProgram/TrainingProgram';

const HomePage = () => {
  return (
    <div>
      <div>< Menu /></div>
      <div><ImageSlideShow /></div>g
      <div style={{backgroundColor: "black", textAlign: "center", paddingTop: "10px"}}>
          <h1 style={{color: "white"}}>Workout Vlogs</h1>
      </div>
      <div><ExerciseGrid /></div>
      <div><TrainingProgram /></div>
      <div> <Footer /></div>
    </div>
  );
};

export default HomePage;