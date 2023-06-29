import React, { useState, useRef, useEffect, Component } from "react";
import { Chatbot } from "react-chatbot-kit";
import { createChatBotMessage } from "react-chatbot-kit";
// import { FlightBotAvatar } from './FlightBotAvatar';
import "react-chatbot-kit/build/main.css";
import ActionProvider from "./ActionProvider";
import MessageParser from "./MessageParser";
import "./chatbot.css";

const ChatbotInterface = ({ onClose, ReassignSessionID }) => {
  const chatbotRef = useRef(null);
  let [showChat, setShowChat] = useState(false);
  const [maximized, setMaximized] = useState(false);
  // const [show, toggleShow] = useState(false);
  // const [showChatbot, setShowChatbot] = useState(false);

  const MyAvatar = (props) => {
    const { imageUrl, altText } = props;
  
    return <img className="avatar-image" src={"data:image/svg+xml,%3csvg version='1' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3e%3cpath d='M303 70a47 47 0 1 0-70 40v84h46v-84c14-8 24-23 24-40z' fill='%2393c7ef'/%3e%3cpath d='M256 23v171h23v-84a47 47 0 0 0-23-87z' fill='%235a8bb0'/%3e%3cpath fill='%2393c7ef' d='M0 240h248v124H0z'/%3e%3cpath fill='%235a8bb0' d='M264 240h248v124H264z'/%3e%3cpath fill='%2393c7ef' d='M186 365h140v124H186z'/%3e%3cpath fill='%235a8bb0' d='M256 365h70v124h-70z'/%3e%3cpath fill='%23cce9f9' d='M47 163h419v279H47z'/%3e%3cpath fill='%2393c7ef' d='M256 163h209v279H256z'/%3e%3cpath d='M194 272a31 31 0 0 1-62 0c0-18 14-32 31-32s31 14 31 32z' fill='%233c5d76'/%3e%3cpath d='M380 272a31 31 0 0 1-62 0c0-18 14-32 31-32s31 14 31 32z' fill='%231e2e3b'/%3e%3cpath d='M186 349a70 70 0 1 0 140 0H186z' fill='%233c5d76'/%3e%3cpath d='M256 349v70c39 0 70-31 70-70h-70z' fill='%231e2e3b'/%3e%3c/svg%3e"} alt={"B"} />;
  };

  const MyCustomAvatar = (props) => {
    const { imageUrl, altText } = props;
  
    return <img className="avatar-image" src={"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5OHzSWGjwIFkz-090vRjzw_WyP7DodXEATw&usqp=CAU"} alt={"U"} />;
  };


  const config = {
    botName: "ChatBot",
    initialMessages: [createChatBotMessage(`Hello There, How can I help you`)],
    customStyles: {
      botMessageBox: {
        backgroundColor: "#7399C6",
        // botAvatar={(props) => (
        //   <img src={updatedBotAvatarProps.imageUrl} alt={updatedBotAvatarProps.altText} />
        // )}
      },
      chatButton: {
        backgroundColor: "#7399C6",
      },
    },
    customComponents: {
      // Replaces the default header
      botAvatar: (props) => <MyAvatar {...props} />,
      userAvatar: (props) => <MyCustomAvatar {...props} />,
      header: () => (
        <div
          style={{
            backgroundColor: "#7399C6",
            padding: "5px",
            borderRadius: "3px",
            height : "5vh",
            color: "#fff",
            size: "4px",
            family: "cursive",
            fontSize: "25px"
          }}
        >
          FinBOT 🤖
          <button
            class="btn2"
            data-testid="chat-toggle-button11"
            onClick={toggleChatbot}
          >
            <i class="fa fa-times"></i>
          </button>
          <button
            className="btn2"
            data-testid="chat-toggle-button2"
            onClick={toggleMaximize}
          >
            <i className={`fa ${maximized ? "fa-compress" : "fa-expand"}`}></i>
          </button>
          <button
            className="btn2"
            data-testid="chat-toggle-button"
            onClick={() => startChat()}
          >
            <i className="fa fa-minus"></i>
          </button>
        </div>
      ),
    },
  };

  const startChat = () => {
    console.log("open");
    setShowChat(true);
  };
  const hideChat = () => {
    console.log("closed");
    setShowChat(false);
  };
  const toggleMaximize = () => {
    setMaximized(!maximized);
  };

  const toggleChatbot = () => {
    refreshPage();
  };

  function refreshPage() {
    window.location.reload(false);
  }

  const updatedBotAvatarProps = {
    imageUrl: 'https://st3.depositphotos.com/8950810/17657/v/450/depositphotos_176577870-stock-illustration-cute-smiling-funny-robot-chat.jpg',
    altText: 'New Avatar',
  };

  return (
    <>
      <div
        className={`chatbot-wrapper${maximized ? " maximized" : ""}`}
        style={{ display: showChat ? "none" : "" }}
      >
        <div className={`chatbot-container`}>
          <Chatbot
            botAvatar="bot.svg"
            config={config}
            actionProvider={ActionProvider}
            messageParser={MessageParser}
          />
        </div>
      </div>
      <div className="button-container">
        {showChat ? (
          <div className="chatbot-toggle">
            <button
              className="btn"
              data-testid="chat-toggle-button3"
              onClick={() => hideChat()}
            >
              continue...
            </button>
          </div>
        ) : (
          <p></p>
        )}
      </div>
    </>
  );
};

export default ChatbotInterface;