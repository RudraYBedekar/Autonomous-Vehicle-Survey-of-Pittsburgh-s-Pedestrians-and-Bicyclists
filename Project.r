# Load required libraries
library(ggplot2)
library(dplyr)

# Load the dataset
# Replace backslashes with forward slashes in the path to avoid errors
data <- read.csv("C:/Users/rudra/OneDrive/Desktop/gmu syllabus/infs 580/dataset/avsurvey2019data.csv")

# Filter data for relevant columns
relevant_columns <- c("ShareTripData", "ReportSafetyIncident", "FamiliarityNews")
filtered_data <- data %>% filter(!is.na(ShareTripData) & !is.na(FamiliarityNews))

# Encode categorical variables (if needed for modeling purposes)
filtered_data <- filtered_data %>%
  mutate(
    ShareTripData_Encoded = as.numeric(factor(ShareTripData)),
    FamiliarityNews_Encoded = as.numeric(factor(FamiliarityNews))
  )

# Group data by willingness to share trip data and familiarity with news
grouped_data <- filtered_data %>%
  group_by(ShareTripData, FamiliarityNews) %>%
  summarise(Count = n(), .groups = 'drop')

# Plot a bar chart
ggplot(grouped_data, aes(x = ShareTripData, y = Count, fill = FamiliarityNews)) +
  geom_bar(stat = "identity", position = "dodge") +
  scale_fill_viridis_d(name = "Knowledge of the News") +
  labs(
    title = "Connection Between AV News Knowledge and Sharing Trip Data",
    x = "Availability to Share Travel Information",
    y = "Responses Count"
  ) +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  geom_text(aes(label = Count), position = position_dodge(0.9), vjust = -0.3)
