import React from "react";
import './SkeletonLoader.css'

function SkeletonLoader() {
    return (
        <div className="skeleton-loader">
            <div className="skeleton-card" />
            <div className="skeleton-card" />
            <div className="skeleton-card" />
        </div>
    )
}

export default SkeletonLoader