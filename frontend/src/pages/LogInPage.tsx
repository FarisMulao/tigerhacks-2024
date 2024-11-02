import React from "react";
import {
  Card,
  CardContent,
  Typography,
  TextField,
  Button,
  Checkbox,
  FormControlLabel,
  Box,
} from "@mui/material";
import Navbar from "../components/Navbar";

const LogInPage = () => {
  return (
    <div>
      <Navbar />
      <Box
        display="flex"
        alignItems="center"
        justifyContent="center"
        minHeight="calc(100vh - 64px)"
        bgcolor="#f7f9fc"
      >
        <Card sx={{ padding: 3, boxShadow: 3, borderRadius: 2, maxWidth: 400 }}>
          <CardContent>
            <Typography
              variant="h5"
              align="center"
              fontWeight="bold"
              gutterBottom
            >
              Log In
            </Typography>

            <TextField
              label="Email"
              variant="outlined"
              fullWidth
              sx={{
                "& .MuiOutlinedInput-root": {
                  borderRadius: "8px",
                  "& fieldset": {
                    borderColor: "#e0e0e0",
                  },
                  "&:hover fieldset": {
                    borderColor: "#bdbdbd",
                  },
                },
                marginBottom: 2,
              }}
            />

            <TextField
              label="Password"
              type="password"
              variant="outlined"
              fullWidth
              sx={{
                "& .MuiOutlinedInput-root": {
                  borderRadius: "8px",
                  "& fieldset": {
                    borderColor: "#e0e0e0",
                  },
                  "&:hover fieldset": {
                    borderColor: "#bdbdbd",
                  },
                },
                marginBottom: 2,
              }}
            />

            <FormControlLabel
              control={<Checkbox color="primary" />}
              label="Remember me"
              sx={{ marginBottom: 2 }}
            />

            <Button
              variant="contained"
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
              Log In
            </Button>

            <Typography align="center" variant="body2" sx={{ marginBottom: 2 }}>
              Don't have an account?{" "}
              <a
                href="/signup"
                style={{ textDecoration: "none", color: "#1976d2" }}
              >
                Sign up
              </a>
            </Typography>
          </CardContent>
        </Card>
      </Box>
    </div>
  );
};

export default LogInPage;
