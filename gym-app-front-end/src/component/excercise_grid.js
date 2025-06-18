import React from "react";

function ExerciseGrid() {


    return (

        <div style={styles.videoContainer}>
            <div>
                <video style={styles.video}>
                    <source
                        src='https://d2hozp596kp382.cloudfront.net/C0142.MP4'
                        type='video/mp4'
                    />
                </video>
                <div style={styles.videoCaption}>
                    Push Day With The Guys
                </div>
                <div style={styles.videoDate}>
                    13/01/2025
                </div>
            </div>
            <div>
                <video style={styles.video}>
                    <source
                        src='https://d2hozp596kp382.cloudfront.net/C0142.MP4'
                        type='video/mp4'
                    />
                </video>
                <div style={styles.videoCaption}>
                    Cable Chest Press
                </div>
                <div style={styles.videoDate}>
                    13/01/2025
                </div>
            </div>
            <div>
                <video style={styles.video}>
                    <source
                        src='https://d2hozp596kp382.cloudfront.net/C0142.MP4'
                        type='video/mp4'
                    />
                </video>
                <div style={styles.videoCaption}>
                    Cable Chest Press
                </div>
                <div style={styles.videoDate}>
                    13/01/2025
                </div>
            </div>
        </div>
    )
}

const styles = {
    videoContainer: {
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'flex-start',
        flexWrap: 'nowrap',
        width: '100vw',
        padding: '20px',
        boxSizing: 'border-box',
        gap: '20px'
      },      
    video: {
        width: '100%',
        height: 'auto',
        borderRadius: '8px'
    },
    videoCaption: {
        fontWeight: "bold",
        textDecoration: "underline"
    },
    videoDate: {
        fontSize: "12px",
        lineHeight: "16px",
        marginTop: "4px"
    },
    videoItem: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        flex: '1 1 0',
        maxWidth: '30%',  // Adjust based on how many videos you're showing
      }
      
}

export default ExerciseGrid