import "./App.css";
import { Navigate, Route, Routes } from "react-router-dom";
import HomePage from "./pages/HomePage";
import PersonalPlantsPage from "./pages/PersonalPlantsPage";
import UploadPage from "./pages/UploadPage";
import { useEffect, useState } from "react";
import Navbar from "./components/Navbar";

function App() {
  const [userInfo, setUserInfo] = useState<{
    email: string;
    name: string;
  } | null>(null);

  async function getUserInfo() {
    let headers = new Headers();

    let data = await fetch("https://www.plid.us/getUserInfo", {
      method: "GET",
      headers: headers,
      credentials: "include",
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch user information");
        }
        return response.json();
      })
      .then((json) => {
        console.log(json);
        const userInfo = {
          name: json.name,
          email: json.email,
        };
        return userInfo;
      })
      .catch((error) => {
        console.error(error);
        return null;
      });

    setUserInfo(data);
    console.log(userInfo);
  }

  useEffect(() => {
    getUserInfo();
  }, []);

  return (
    <div className="App">
      <Navbar email={userInfo?.email} name={userInfo?.name}></Navbar>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/index.html" element={<Navigate to="/" />} />
        <Route
          path="/myplants"
          element={<PersonalPlantsPage></PersonalPlantsPage>}
        />
        <Route
          path="/upload"
          element={
            <UploadPage
              email={userInfo?.email}
              name={userInfo?.name}
            ></UploadPage>
          }
        />
      </Routes>
    </div>
  );
}

export default App;
