import React from "react";
import { Box, Card, CardContent, Typography, Button } from "@mui/material";
import Navbar from "../components/Navbar";

const HomePage = () => {
  return (
    <div>
      <Navbar />
      <Box
        display="flex"
        flexDirection="column"
        alignItems="center"
        justifyContent="center"
        minHeight="calc(100vh - 64px)"
        bgcolor="#f7f9fc"
        px={3}
      ></Box>
    </div>
  );
};

export default HomePage;
