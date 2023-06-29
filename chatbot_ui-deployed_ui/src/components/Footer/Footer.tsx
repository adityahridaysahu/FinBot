import React from "react";
import "./Footer.css";

const Footer: React.FC = () => {
  return (
    <footer className="footer">
      <div className="footer__content">
        <div className="footer__section">
          <h3>About Us</h3>
          <p>
            Goldman Sachs leaders, investors and analysts break down the key
            issues moving markets in our weekly podcast The Markets, a new
            series from Goldman Sachs Exchanges.
          </p>
        </div>
        <div className="footer__section">
          <h3>Contact</h3>
          <p>Email: info@example.com</p>
          <p>Phone: +1 123-456-7890</p>
        </div>
        <div className="footer__section">
          <h3>Follow Us</h3>
          <div className="footer__social-icons">
            <a href="#" target="_blank" rel="noopener noreferrer">
              <i className="fab fa-facebook"></i>
            </a>
            <a href="#" target="_blank" rel="noopener noreferrer">
              <i className="fab fa-twitter"></i>
            </a>
            <a href="#" target="_blank" rel="noopener noreferrer">
              <i className="fab fa-instagram"></i>
            </a>
          </div>
        </div>
      </div>
      <div className="footer__bottom">
        <p>&copy; 2023 GS. All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;
