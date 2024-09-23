// HomePage.js
import React from 'react';
import Menu from './Menu';
import Exercises from './component/exercises';
import ImageSlideShow from './component/ImageSlideShow';
import ExerciseGrid from './component/excercise_grid';
import Footer from './component/footer';

const HomePage = () => {
  return (
    <div>
      <div>< Menu /></div>
      <div><ImageSlideShow /></div>
      <div style={{backgroundColor: "black", textAlign: "center", paddingTop: "10px"}}>
          <h1 style={{color: "white"}}>Workout Vlogs</h1>
          <div><ExerciseGrid /></div>
      </div>
      <div>< Exercises /></div>
      <div> <Footer /></div>
    </div>
  );
};

export default HomePage;