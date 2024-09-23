import React from "react";
import '../css/Footer.css'; // Optional: Use CSS for styling


const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <p>&copy; {new Date().getFullYear()} JussGym. All rights reserved.</p>
        <ul className="footer-links">
          <li><a href="/privacy-policy">Privacy Policy</a></li>
          <li><a href="/terms-of-service">Terms of Service</a></li>
          <li><a href="/contact-us">Contact Us</a></li>
        </ul>
      </div>
    </footer>
  );
};

export default Footer;
