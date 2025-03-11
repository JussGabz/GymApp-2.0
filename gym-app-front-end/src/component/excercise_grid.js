import React from "react";

function ExerciseGrid() {


    return (

        <div style={styles.videoContainer}>
            <div>
                <video style={styles.video}>
                    <source
                        src='https://d164p06em7ia.cloudfront.net/C0201.MP4'
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
                        src='https://d164p06em7ia.cloudfront.net/C0142.MP4'
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
                        src='https://d164p06em7ia.cloudfront.net/C0143.MP4'
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
        justifyContent: 'center',
        alignItems: 'center',
        height: '50vh',
        // backgroundColor: '#000'
    },
    video: {
        maxWidth: '607px',
        maxHeight: '341px',
        marginRight: "20px"
    },
    videoCaption: {
        fontWeight: "bold",
        textDecoration: "underline"
    },
    videoDate: {
        fontSize: "12px",
        lineHeight: "16px",
        marginTop: "4px"
    }
}

export default ExerciseGrid