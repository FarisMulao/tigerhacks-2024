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

const plantData = [
  {
    commonName: "African Violet",
    scientificName: "Saintpaulia Ionatha",
    wateringScheduleSummer: 7,
    wateringScheduleWinter: 14,
    lightNeeds: "Indirect sunlight",
    lastWateredDate: "2024-10-25",
  },
  {
    commonName: "Aloe Vera",
    scientificName: "Aloe Vera",
    wateringScheduleSummer: 7,
    wateringScheduleWinter: 14,
    lightNeeds: "Direct sunlight",
    lastWateredDate: "2024-10-25",
  },
  {
    commonName: "Anthurium",
    scientificName: "Anthurium Andraeanum",
    wateringScheduleSummer: 9,
    wateringScheduleWinter: 12,
    lightNeeds: "Indirect sunlight",
    lastWateredDate: "2024-10-25",
  },
  {
    commonName: "Bird of Paradise",
    scientificName: "Strelitzia reginae",
    wateringScheduleSummer: 5,
    wateringScheduleWinter: 10,
    lightNeeds: "Bright, direct sunlight",
    lastWateredDate: "2024-10-25",
  },
  {
    commonName: "Boston Fern",
    scientificName: "Nephrolepis exaltata",
    wateringScheduleSummer: 5,
    wateringScheduleWinter: 7,
    lightNeeds: "Indirect sunlight",
    lastWateredDate: "2024-10-25",
  },
  {
    commonName: "Chinese Money Plant",
    scientificName: "",
    wateringScheduleSummer: 7,
    wateringScheduleWinter: 14,
    lightNeeds: "Bright, indirect sunlight",
    lastWateredDate: "2024-10-25",
  },
  {
    commonName: "Monstera Deliciosa",
    scientificName: "Monstera Deliciosa",
    wateringScheduleSummer: 10,
    wateringScheduleWinter: 14,
    lightNeeds: "Bright, indirect sunlight",
    lastWateredDate: "2024-10-25",
  },
  {
    commonName: "Poinsettia",
    scientificName: "",
    wateringScheduleSummer: 5,
    wateringScheduleWinter: 7,
    lightNeeds: "Indirect sunlight",
    lastWateredDate: "2024-10-25",
  },
  {
    commonName: "Prayer Plant",
    scientificName: "",
    wateringScheduleSummer: 7,
    wateringScheduleWinter: 10,
    lightNeeds: "Low to moderate light",
    lastWateredDate: "2024-10-25",
  },
  {
    commonName: "Tradescantia",
    scientificName: "",
    wateringScheduleSummer: 7,
    wateringScheduleWinter: 10,
    lightNeeds: "Bright, indirect sunlight",
    lastWateredDate: "2024-10-25",
  },
];

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
      console.log(data);

      const fetchedPlants = data.plantData.map((item: any) => {
        const plantIndex = parseInt(item.planttype, 10);
        const plantDetails = plantData[plantIndex];

        const startDate = new Date(item.startdate);
        const currentDate = new Date();
        const daysSinceWatered = Math.floor(
          (currentDate.getTime() - startDate.getTime()) / (1000 * 60 * 60 * 24)
        );

        const needsWatering =
          daysSinceWatered % plantDetails.wateringScheduleSummer === 0;

        return {
          ...plantDetails,
          lastWateredDate: item.startdate,
          needsWatering,
        };
      });

      console.log(fetchedPlants);
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
