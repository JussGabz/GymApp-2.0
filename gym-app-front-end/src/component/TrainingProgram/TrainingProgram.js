import { Button } from "react-bootstrap"


const TrainingProgram = () => {
    return (
        <div style={{ display: "flex" }}>
            <div style={{ flex: 1, padding: "10px", borderRight: "2px solid black" }}>
                <div style={{ display: "flex", justifyContent: "center", alignItems: "center"}}>
                    <img src={"https://d2hozp596kp382.cloudfront.net/1.png"} alt="" style={{ width: '100px', borderRadius: '8px'}}/>
                </div>
            </div>
            <div style={{ flex: 1, padding: "10px" }}>
                <p>START TODAY</p>
                <h2>Training Programs</h2>
                <div>Download one of the Training Programs - Get In the Best Shape of your Life!</div>
                <Button>Download</Button>
            </div>
        </div>

    )
}
export default TrainingProgram