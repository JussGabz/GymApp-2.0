import React, { useState, useEffect } from "react";

function ImageSlideShow() {
    const images = [
        "images/pexels-anush-1229356.jpg",
        "images/pexels-victorfreitas-791763.jpg",
        "images/pexels-victorfreitas-841130.jpg",
    ]

    const [currentIndex, setCurrentIndex] = useState(0)

    useEffect(() => {
        const interval = setInterval(() => {
            setCurrentIndex((prevIndex) => (prevIndex +1) % images.length)
        }, 3000) // Change Image every 3 secs

        return () => clearInterval(interval)
    }, [images.length])

    const nextSlide = () => {
        setCurrentIndex((currentIndex + 1) % images.length)
    }

    const prevSlide = () => {
        setCurrentIndex(
            (currentIndex - 1 + images.length) % images.length
        )
    }

    return (
        <div style={styles.container}>
            <img
                src={images[currentIndex]}
                alt="slideshow"
                style={styles.image}
            />
            <button style={styles.prevButton} onClick={prevSlide}>
                Prev
            </button>
            <button style={styles.nextButton} onClick={nextSlide}>
                Next
            </button>
        </div>
    )
}

const styles = {
    container: {
      position: "relative",
      width: "100%",
      height: "30vw",
    //   overflow: "hidden",
      margin: "0",
      padding: "0",
      boxSizing: "border-box"
    },
    image: {
      width: "100%",
      height: "100%",
      objectFit: "cover",
      margin: "0",         // No margin on the image
      padding: "0",        // No padding on the image
      display: "block",    // Prevent inline image spacing issues
    },
    prevButton: {
      position: "absolute",
      top: "50%",
      left: "0",
      transform: "translateY(-50%)",
      backgroundColor: "rgba(0, 0, 0, 0.5)",
      color: "white",
      border: "none",
      padding: "10px",
      cursor: "pointer",
    },
    nextButton: {
      position: "absolute",
      top: "50%",
      right: "0",
      transform: "translateY(-50%)",
      backgroundColor: "rgba(0, 0, 0, 0.5)",
      color: "white",
      border: "none",
      padding: "10px",
      cursor: "pointer",
    },
  };

export default ImageSlideShow