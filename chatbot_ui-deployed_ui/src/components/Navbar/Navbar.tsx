// import React from "react";
// import "./Navbar.css";

// const Navbar: React.FC = () => {
//   return (
//     <nav>
//       <h1>Goldman Sachs</h1>
//     </nav>
//   );
// };

// export default Navbar;

// import React, { useState } from "react";
// import "./Navbar.css";

// const Navbar: React.FC = () => {
//   const [dropdownOpen, setDropdownOpen] = useState(false);
//   const [hoverText, setHoverText] = useState("");
//   const [hoverPosition, setHoverPosition] = useState({ top: 0, left: 0 });

//   const toggleDropdown = () => {
//     setDropdownOpen(!dropdownOpen);
//   };

//   const handleHover = (text: string, event: React.MouseEvent) => {
//     setHoverText(text);
//     const linkRect = event.currentTarget.getBoundingClientRect();
//     const position = {
//       top: linkRect.top + window.pageYOffset,
//       left: linkRect.left + window.pageXOffset - 200, // Adjust the value here to control the position
//     };
//     setHoverPosition(position);
//   };

//   return (
//     <nav>
//       <div className="navbar-left">
//         <h1>Goldman Sachs</h1>
//       </div>
//       <div className="navbar-right">
//         <button className="dropdown-button" onClick={toggleDropdown}>
//           Menu &#9662;
//         </button>
//         {dropdownOpen && (
//           <div className="dropdown-menu">
//             <a
//               href="#about-us"
//               // onMouseEnter={(e) =>
//               //   handleHover(
//               //     "My name is GOLDMAN SACHS I worked there to a point where is dont",
//               //     e
//               //   )
//               // }
//               // onMouseLeave={() => setHoverText("")}
//             >
//               About Us
//             </a>
//             <a href="#what-we-do">What We Do</a>
//             <a href="#faq">FAQ</a>
//           </div>
//         )}
//       </div>
//       {hoverText && (
//         <div
//           className="hover-text"
//           style={{ top: hoverPosition.top, left: hoverPosition.left }}
//         >
//           {hoverText}
//         </div>
//       )}
//     </nav>
//   );
// };

// export default Navbar;

import React, { useState } from "react";
import "./Navbar.css";
import logo from "./logo.png"; // Assuming you have the logo image file
import { FaBars } from "react-icons/fa";

const Navbar: React.FC = () => {
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const [hoverText, setHoverText] = useState("");
  const [hoverPosition, setHoverPosition] = useState({ top: 0, left: 0 });

  const toggleDropdown = () => {
    setDropdownOpen(!dropdownOpen);
  };

  const handleHover = (text: string, event: React.MouseEvent) => {
    setHoverText(text);
    const position = {
      top: event.clientY,
      left: event.clientX,
    };
    setHoverPosition(position);
  };

  return (
    <nav>
      <div className="navbar-left">
        <div className="logo-container">
          <img src={logo} alt="Logo" className="logo" />
          <h1>Goldman Sachs</h1>
        </div>
      </div>
      <div className="navbar-right">
        <button
          data-testid="dropdown-btn"
          className="dropdown-button"
          onClick={toggleDropdown}
        >
          <FaBars />
        </button>
        {dropdownOpen && (
          <div className="dropdown-menu">
            <a
              href="#about-us"
              // onMouseEnter={(e) => handleHover("Lorem ipsum dolor sit amet", e)}
              // onMouseLeave={() => setHoverText("")}
            >
              About Us
            </a>
            <a href="#what-we-do">What We Do</a>
            <a href="#faq">FAQ</a>
          </div>
        )}
      </div>
      {hoverText && (
        <div
          className="hover-text"
          style={{ top: hoverPosition.top, left: hoverPosition.left }}
        >
          {hoverText}
        </div>
      )}
    </nav>
  );
};

export default Navbar;
