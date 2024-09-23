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
            <video style={styles.video}>
                <source
                    src='https://d164p06em7ia.cloudfront.net/C0142.MP4'
                    type='video/mp4'
                />
            </video>
            <video style={styles.video}>
                <source
                    src='https://d164p06em7ia.cloudfront.net/C0143.MP4'
                    type='video/mp4'
                />
            </video>
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
        backgroundColor: '#000'
    },
    video: {
        maxWidth: '600px',
        maxHeight: '300px',
        padding: '5px'
    }
}

export default ExerciseGrid