import React, { useEffect, useState } from "react";
import MyPlant from "../components/MyPlant";
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

  async function fetchPlants() {
    try {
      const response = await fetch("/getUserPlants", {
        method: "GET",
      });
      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }

      const data = await response.json();

      const fetchedPlants = data.plantData.map((item: any) => ({
        commonName: item.commonName,
        scientificName: item.scientificName,
        wateringScheduleSummer: item.wateringScheduleSummer,
        wateringScheduleWinter: item.wateringScheduleWinter,
        lightNeeds: item.lightNeeds,
        lastWateredDate: item.startdate,
      }));

      setPlants(fetchedPlants);
    } catch (error) {
      console.error("Error fetching plant data:", error);
    }
  }

  useEffect(() => {
    fetchPlants();
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
