import React from "react";
import MyPlant from "../components/MyPlant";
import Navbar from "../components/Navbar";
import { Box, Typography } from "@mui/material";

const samplePlant = {
  commonName: "Aloe Vera",
  scientificName: "Aloe Vera",
  wateringScheduleSummer: 7,
  wateringScheduleWinter: 14,
  lightNeeds: "Direct sunlight",
  lastWateredDate: "2024-10-25", // Format as needed, or change to Date type if preferred
};

const samplePlant2 = {
  commonName: "Laceleaf",
  scientificName: "Anthurium",
  wateringScheduleSummer: 9,
  wateringScheduleWinter: 12,
  lightNeeds: "Indirect sunlight",
  lastWateredDate: "2024-10-25", // Format as needed, or change to Date type if preferred
};

interface Props {}

function PersonalPlantsPage(props: Props) {
  return (
    <div>
      <Navbar />
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
        >
          My Plants
        </Typography>
        <MyPlant plant={samplePlant} />
        <MyPlant plant={samplePlant2} />
      </Box>
    </div>
  );
}

export default PersonalPlantsPage;
