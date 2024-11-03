import { useState } from "react";
import { Box, Button, Card, CardContent, Typography } from "@mui/material";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";
import ImageIcon from "@mui/icons-material/Image";
import Navbar from "../components/Navbar";
import { useNavigate } from "react-router-dom";

interface Props {
  email?: string;
  name?: string;
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

function UploadPage({ email, name }: Props) {
  const [selectedImage, setSelectedImage] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [plantID, setPlantID] = useState<number | null>(null);
  const navigate = useNavigate();

  const handleImageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setSelectedImage(file);
      setPreview(URL.createObjectURL(file));
    }
  };

  async function sendImageToBackend(imageFile: File) {
    const formData = new FormData();
    formData.append("image", imageFile);

    try {
      const response = await fetch("http://localhost:5000/uploadimage", {
        method: "POST",
        body: formData,
      });
      if (!response.ok) {
        throw new Error(`status: ${response.status}`);
      }

      const result = await response.text();
      console.log(result);
      return result;
    } catch (error) {
      console.error("Error sending image:", error);
    }
  }

  const handleSubmit = async () => {
    if (selectedImage) {
      console.log("Submitting image to backend:", selectedImage);
      const id = await sendImageToBackend(selectedImage);
      setPlantID(Number(id));
    } else {
      console.log("No image selected");
    }
  };

  const keepPlant = () => {
    if (plantID !== null) {
      const plantInfo = plantData[plantID];

      const existingPlants = JSON.parse(
        sessionStorage.getItem("savedPlants") || "[]"
      );

      existingPlants.push({
        ...plantInfo,
        lastWateredDate: new Date().toISOString().split("T")[0],
      });

      sessionStorage.setItem("savedPlants", JSON.stringify(existingPlants));

      navigate("/myplants");
    }
  };

  return (
    <div>
      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        minHeight="calc(100vh - 64px)"
        bgcolor="#f7f9fc"
      >
        <Card
          sx={{
            padding: 4,
            boxShadow: 3,
            borderRadius: 2,
            maxWidth: 400,
            minWidth: 400,
            mt: -10,
          }}
        >
          <CardContent>
            <Typography
              variant="h5"
              align="center"
              fontWeight="bold"
              gutterBottom
            >
              Upload an Image
            </Typography>

            <Box sx={{ mb: 2 }}>
              <input
                accept="image/*"
                style={{ display: "none" }}
                id="upload-button"
                type="file"
                onChange={handleImageChange}
              />
              <label htmlFor="upload-button">
                <Button
                  variant="contained"
                  component="span"
                  startIcon={<CloudUploadIcon />}
                  fullWidth
                  sx={{
                    backgroundColor: "#000",
                    color: "#fff",
                    padding: "10px 0",
                    borderRadius: "8px",
                    "&:hover": {
                      backgroundColor: "#333",
                    },
                    marginBottom: 2,
                  }}
                >
                  Choose an Image
                </Button>
              </label>
            </Box>

            {preview ? (
              <Box
                display="flex"
                flexDirection="column"
                alignItems="center"
                sx={{ mb: 2 }}
              >
                <img
                  src={preview}
                  alt="Preview"
                  style={{
                    width: "100%",
                    maxHeight: 200,
                    objectFit: "cover",
                    borderRadius: "8px",
                    marginBottom: 10,
                  }}
                />
                <Typography variant="body2" color="textSecondary">
                  {selectedImage?.name}
                </Typography>
              </Box>
            ) : (
              <Box
                display="flex"
                flexDirection="column"
                alignItems="center"
                sx={{ mb: 2 }}
              >
                <ImageIcon sx={{ fontSize: 60, color: "grey.400" }} />
                <Typography variant="body2" color="textSecondary">
                  No image selected
                </Typography>
              </Box>
            )}

            <Button
              variant="contained"
              fullWidth
              onClick={handleSubmit}
              disabled={!selectedImage}
              sx={{
                backgroundColor: "#000",
                color: "#fff",
                padding: "10px 0",
                borderRadius: "8px",
                "&:hover": {
                  backgroundColor: "#333",
                },
                marginBottom: 2,
              }}
            >
              Submit Image
            </Button>

            {plantID !== null && (
                <Box mt={4}>
                  <Typography variant="h6" fontWeight="bold">
                    Your plant has been identified as{" "}
                    {plantData[plantID].commonName}
                  </Typography>
                </Box>
              ) && <Button onClick={() => keepPlant()}>Keep Plant</Button>}
          </CardContent>
        </Card>
      </Box>
    </div>
  );
}

export default UploadPage;
