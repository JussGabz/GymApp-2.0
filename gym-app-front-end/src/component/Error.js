import React from "react";

function Error({message = "Something went wrong."}) {
    return <div className="alert alert-danger">{message}</div>
}

export default Error