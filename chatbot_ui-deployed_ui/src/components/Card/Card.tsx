import React from "react";
import "./Card.css";

interface Props {
  natural: boolean;
  dateBuilt: string;
  imageUrl: string;
  title: string;
  location: string;
  googleMapsUrl: string;
  description: string;
  key: number;
}

const Card: React.FC<Props> = (props) => {
  let dateText;
  if (props.natural === true) {
    dateText = "NATURAL";
  } else {
    dateText = `COMPLETED IN ${props.dateBuilt}`;
  }

  return (
    <div className="card">
      <img src={props.imageUrl} className="card--image" alt={props.title} />
      <div className="card--info">
        <p className="card--title">{props.title}</p>
        <p className="card--description">{props.description}</p>
      </div>
    </div>
  );
};

export default Card;
