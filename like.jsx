import { useState } from "react";
import "./like.css";

function Like() {
  let [isFilled, setIsFilled] = useState(false);

  function Heart() {
    setIsFilled(!isFilled);
  }

  let obj = { color: "red", display: "flex", justifyContent: "Center" };
  function FilledHeart() {
    return (
      <div className="container">
        <div className="box">
          <i class="bx bxs-heart"></i>
        </div>
      </div>
    );
  }

  function EmptyHeart() {
    return (
      <div className="container">
        <div className="box">
          <i class="bx bx-heart"></i>
        </div>
      </div>
    );
  }

  return (
    <div>
      <p onClick={Heart}>{isFilled ? <FilledHeart /> : <EmptyHeart />}</p>
    </div>
  );
}

export default Like;
