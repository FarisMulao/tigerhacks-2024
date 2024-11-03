import React from "react";
import { Box, Card, CardContent, Typography, Button } from "@mui/material";
import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css";
import Navbar from "../components/Navbar";
import plant1 from "../components/images/stock-plant-1.jpg";
import plant2 from "../components/images/stock-plant-2.jpg";
import plant3 from "../components/images/stock-plant-3.jpg";

const HomePage: React.FC = () => {
  return (
    <div>
      <Box
        display="flex"
        flexDirection="column"
        alignItems="center"
        justifyContent="center"
        minHeight="calc(100vh - 64px)"
        bgcolor="#f7f9fc"
        px={3}
      >
        <Card
          sx={{
            maxWidth: 600,
            padding: 3,
            boxShadow: 3,
            borderRadius: 2,
            textAlign: "center",
            marginBottom: 4,
          }}
        >
          <CardContent>
            <Typography variant="h4" fontWeight="bold" gutterBottom>
              Welcome to PLID
            </Typography>
            <Typography variant="body1" color="textSecondary">
              PLID is your AI-powered plant identification service. Just take a
              photo, and our app will provide you with detailed information
              about the plant in seconds.
            </Typography>
            <Button
              variant="contained"
              color="primary"
              sx={{ borderRadius: "8px", padding: "10px 20px", mb: 2 }}
              href="/signup"
            >
              Get Started
            </Button>

            <Carousel
              showArrows={false}
              autoPlay
              infiniteLoop
              interval={5000}
              showThumbs={false}
              showStatus={false}
              dynamicHeight
            >
              <div>
                <img
                  src={plant1}
                  alt="Plant 1"
                  style={{
                    maxWidth: "100%",
                    maxHeight: "300px",
                    objectFit: "contain",
                  }}
                />
                <Typography variant="caption">Plant 1</Typography>
              </div>
              <div>
                <img
                  src={plant2}
                  alt="Plant 2"
                  style={{
                    maxWidth: "100%",
                    maxHeight: "300px",
                    objectFit: "contain",
                  }}
                />
                <Typography variant="caption">Plant 2</Typography>
              </div>
              <div>
                <img
                  src={plant3}
                  alt="Plant 3"
                  style={{
                    maxWidth: "100%",
                    maxHeight: "300px",
                    objectFit: "contain",
                  }}
                />
                <Typography variant="caption">Plant 3</Typography>
              </div>
            </Carousel>
          </CardContent>
        </Card>
      </Box>
    </div>
  );
};

export default HomePage;
