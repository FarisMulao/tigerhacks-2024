import React, { useEffect, useState } from "react";
import MyPlant from "../components/MyPlant";
import Navbar from "../components/Navbar";
import { Box, Typography } from "@mui/material";

interface Plant {
  commonName: string;
  scientificName: string;
  wateringScheduleSummer: number;
  wateringScheduleWinter: number;
  lightNeeds: string;
  lastWateredDate: string;
}

function PersonalPlantsPage() {
  const [plants, setPlants] = useState<Plant[]>([]);

  // Load plants from session storage on component mount
  useEffect(() => {
    const savedPlants = JSON.parse(
      sessionStorage.getItem("savedPlants") || "[]"
    );
    setPlants(savedPlants);
  }, []);

  return (
    <div>
      <Box
        display="flex"
        flexDirection="column"
        alignItems="center"
        minHeight="calc(100vh - 64px)"
        bgcolor="#f7f9fc"
        px={3}
      >
        <Typography
          variant="h4"
          sx={{ fontWeight: "bold", color: "#000", textDecoration: "none" }}
          gutterBottom
        >
          My Plants
        </Typography>
        {plants.length > 0 ? (
          plants.map((plant, index) => <MyPlant key={index} plant={plant} />)
        ) : (
          <Typography variant="body1" color="textSecondary">
            No plants saved yet.
          </Typography>
        )}
      </Box>
    </div>
  );
}

export default PersonalPlantsPage;
