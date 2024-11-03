import React from "react";
import { Card, Typography, Chip, Avatar, Box } from "@mui/material";
import OpacityIcon from "@mui/icons-material/Opacity"; // water icon
import Brightness7Icon from "@mui/icons-material/Brightness7"; // sunlight icon
import LocalFloristIcon from "@mui/icons-material/LocalFlorist"; // random plant icon

interface Plant {
  commonName: string;
  scientificName: string;
  wateringScheduleSummer: number;
  wateringScheduleWinter: number;
  lightNeeds: string;
  lastWateredDate: string;
}

const isWateringDay = (lastWateredDate: string, interval: number) => {
  const today = new Date();
  const lastWatered = new Date(lastWateredDate);
  const diffDays = Math.floor(
    (today.getTime() - lastWatered.getTime()) / (1000 * 60 * 60 * 24)
  );
  return diffDays >= interval;
};

const MyPlant: React.FC<{ plant: Plant }> = ({ plant }) => {
  const {
    commonName,
    scientificName,
    wateringScheduleSummer,
    wateringScheduleWinter,
    lightNeeds,
    lastWateredDate,
  } = plant;

  const wateringInterval = wateringScheduleSummer;
  const wateringDue = isWateringDay(lastWateredDate, wateringInterval);

  return (
    <Card
      sx={{
        width: "70vw",
        height: "50px",
        mx: "auto",
        my: 2,
        display: "flex",
        alignItems: "center",
        justifyContent: "space-between",
        paddingX: 2,
        boxShadow: 3,
        borderRadius: 2,
      }}
    >
      <Box display="flex" alignItems="center" gap={1}>
        <Avatar sx={{ bgcolor: "green", width: 24, height: 24 }}>
          <LocalFloristIcon fontSize="small" />
        </Avatar>
        <Typography variant="body2" fontWeight="bold">
          {commonName} ({scientificName})
        </Typography>
      </Box>

      <Box display="flex" alignItems="center" gap={0.5}>
        <Brightness7Icon fontSize="small" />
        <Typography variant="body2">Light: {lightNeeds}</Typography>
      </Box>

      <Box display="flex" alignItems="center" gap={1}>
        <OpacityIcon fontSize="small" />
        <Typography variant="body2">
          Summer: {wateringScheduleSummer} days
        </Typography>
        <OpacityIcon fontSize="small" />
        <Typography variant="body2">
          Winter: {wateringScheduleWinter} days
        </Typography>
      </Box>

      <Chip
        label={
          wateringDue
            ? "Water me!"
            : `Next watering in ${
                wateringInterval - (new Date().getDate() % wateringInterval)
              } days`
        }
        color={wateringDue ? "primary" : "default"}
        sx={{
          height: "30px",
          bgcolor: wateringDue ? "primary.main" : "grey.300",
          color: wateringDue ? "white" : "text.secondary",
          fontWeight: "bold",
          paddingX: 2,
        }}
      />
    </Card>
  );
};

export default MyPlant;
