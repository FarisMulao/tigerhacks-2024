import { useState } from "react";
import { Box, Button, Card, CardContent, Typography } from "@mui/material";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";
import ImageIcon from "@mui/icons-material/Image";
import Navbar from "../components/Navbar";

interface Props {}

function UploadPage(props: Props) {
  const [selectedImage, setSelectedImage] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);

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
      const response = await fetch("http://192.168.88.64:5000/upload", {
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

  const handleSubmit = () => {
    if (selectedImage) {
      console.log("Submitting image to backend:", selectedImage);
      sendImageToBackend(selectedImage);
    } else {
      console.log("No image selected");
    }
  };

  return (
    <div>
      <Navbar></Navbar>
      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        minHeight="100vh"
        bgcolor="#f7f9fc"
      >
        <Card
          sx={{
            padding: 4,
            boxShadow: 3,
            borderRadius: 2,
            maxWidth: 400,
            minWidth: 400,
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
          </CardContent>
        </Card>
      </Box>
    </div>
  );
}

export default UploadPage;
