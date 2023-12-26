# import cv2
# import face_recognition

# # Fungsi untuk mendeteksi wajah dan mendapatkan usia
# def detect_faces_and_age(frame):
#     # Mendeteksi wajah menggunakan face_recognition
#     face_locations = face_recognition.face_locations(frame)
    
#     for face_location in face_locations:
#         top, right, bottom, left = face_location

#         # Menggunakan OpenCV untuk mengambil ROI (Region of Interest)
#         face_image = frame[top:bottom, left:right]

#         # Mendeteksi usia menggunakan pustaka OpenCV
#         age_net = cv2.dnn.readNetFromCaffe("./deploy_age.prototxt", "./age_net.caffemodel")
#         blob = cv2.dnn.blobFromImage(face_image, scalefactor=1.0, size=(227, 227), mean=(78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
#         age_net.setInput(blob)
#         age_preds = age_net.forward()

#         # Mendapatkan indeks usia terprediksi
#         age_idx = age_preds[0].argmax()

#         # Mendapatkan usia terprediksi
#         age = age_list[age_idx]

#         # Menampilkan usia pada frame
#         cv2.putText(frame, f"Age: {age}", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     return frame

# # Membaca video dari kamera
# cap = cv2.VideoCapture(0)

# # Daftar usia
# age_list = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(25-32)", "(38-43)", "(48-53)", "(60-100)"]

# while True:
#     # Membaca frame dari kamera
#     ret, frame = cap.read()

#     # Mendeteksi wajah dan usia
#     frame = detect_faces_and_age(frame)

#     # Menampilkan frame
#     cv2.imshow('Video', frame)

#     # Berhenti jika tombol 'q' ditekan
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Menutup kamera dan jendela OpenCV
# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import face_recognition

# # Inisialisasi kamera
# cap = cv2.VideoCapture(0)

# while True:
#     # Baca frame dari kamera
#     ret, frame = cap.read()

#     # Deteksi wajah menggunakan face_recognition
#     face_locations = face_recognition.face_locations(frame)

#     for top, right, bottom, left in face_locations:
#         # Gambar kotak di sekitar wajah
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

#     # Tampilkan frame
#     cv2.imshow('Video', frame)

#     # Hentikan jika tombol 'q' ditekan
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Tutup kamera dan jendela OpenCV
# cap.release()
# cv2.destroyAllWindows()

# import cv2
# import face_recognition

# # Inisialisasi kamera
# cap = cv2.VideoCapture(0)

# while True:
#     # Baca frame dari kamera
#     ret, frame = cap.read()

#     # Deteksi wajah menggunakan face_recognition
#     face_locations = face_recognition.face_locations(frame)

#     for top, right, bottom, left in face_locations:
#         # Gambar kotak di sekitar wajah
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

#     # Tampilkan frame
#     cv2.imshow('Video', frame)

#     # Hentikan jika tombol 'q' ditekan
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Tutup kamera dan jendela OpenCV
# cap.release()
# cv2.destroyAllWindows()

# import cv2
# import face_recognition

# # Inisialisasi kamera
# cap = cv2.VideoCapture(0)

# # Load model untuk mendeteksi usia
# age_net = cv2.dnn.readNetFromCaffe("deploy_age.prototxt", "age_net.caffemodel")
# age_list = ["(0-2)", "(3-6)", "(7-12)", "(13-20)", "(21-32)", "(33-43)", "(44-53)", "(54-100)"]

# # Load model untuk mendeteksi jenis kelamin
# gender_net = cv2.dnn.readNetFromCaffe("deploy_gender.prototxt", "gender_net.caffemodel")
# gender_list = ["Male", "Female"]

# while True:
#     # Baca frame dari kamera
#     ret, frame = cap.read()

#     # Deteksi wajah menggunakan face_recognition
#     face_locations = face_recognition.face_locations(frame)

#     for top, right, bottom, left in face_locations:
#         # Gambar kotak di sekitar wajah
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

#         # Ambil ROI untuk deteksi usia
#         face_image = frame[top:bottom, left:right]

#         # Deteksi usia menggunakan OpenCV
#         blob_age = cv2.dnn.blobFromImage(face_image, scalefactor=1.0, size=(227, 227), mean=(78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
#         age_net.setInput(blob_age)
#         age_preds = age_net.forward()

#         # Dapatkan indeks usia terprediksi
#         age_idx = age_preds[0].argmax()

#         # Dapatkan usia terprediksi
#         age = age_list[age_idx]

#         # Tampilkan usia pada frame
#         cv2.putText(frame, f"Age: {age}", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#         # Ambil ROI untuk deteksi jenis kelamin
#         face_image_gender = frame[top:bottom, left:right]

#         # Deteksi jenis kelamin menggunakan OpenCV
#         blob_gender = cv2.dnn.blobFromImage(face_image_gender, scalefactor=1.0, size=(227, 227), mean=(78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
#         gender_net.setInput(blob_gender)
#         gender_preds = gender_net.forward()

#         # Dapatkan indeks jenis kelamin terprediksi
#         gender_idx = gender_preds[0].argmax()

#         # Dapatkan jenis kelamin terprediksi
#         gender = gender_list[gender_idx]

#         # Tampilkan jenis kelamin pada frame
#         cv2.putText(frame, f"Gender: {gender}", (left, top + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

#     # Tampilkan frame
#     cv2.imshow('Video', frame)

#     # Hentikan jika tombol 'q' ditekan
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Tutup kamera dan jendela OpenCV
# cap.release()
# cv2.destroyAllWindows()


import cv2
import face_recognition
from keras.models import load_model
import numpy as np

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

# Load model untuk mendeteksi usia
age_net = cv2.dnn.readNetFromCaffe("deploy_age.prototxt", "age_net.caffemodel")
age_list = ["(0-2)", "(3-6)", "(7-12)", "(13-20)", "(21-32)", "(33-43)", "(44-53)", "(54-100)"]

# Load model untuk mendeteksi jenis kelamin
gender_net = cv2.dnn.readNetFromCaffe("deploy_gender.prototxt", "gender_net.caffemodel")
gender_list = ["Male", "Female"]

# Load model untuk mendeteksi ekspresi wajah
emotion_model = load_model("model_v_47.hdf5")  # Ganti dengan path yang sesuai
emotion_labels = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

while True:
    # Baca frame dari kamera
    ret, frame = cap.read()

    # Deteksi wajah menggunakan face_recognition
    face_locations = face_recognition.face_locations(frame)

    for top, right, bottom, left in face_locations:
        # Gambar kotak di sekitar wajah
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Ambil ROI untuk deteksi usia
        face_image = frame[top:bottom, left:right]

        # Deteksi usia menggunakan OpenCV
        blob_age = cv2.dnn.blobFromImage(face_image, scalefactor=1.0, size=(227, 227), mean=(78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
        age_net.setInput(blob_age)
        age_preds = age_net.forward()

        # Dapatkan indeks usia terprediksi
        age_idx = age_preds[0].argmax()

        # Dapatkan usia terprediksi
        age = age_list[age_idx]

        # Tampilkan usia pada frame
        cv2.putText(frame, f"Age: {age}", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Ambil ROI untuk deteksi jenis kelamin
        face_image_gender = frame[top:bottom, left:right]

        # Deteksi jenis kelamin menggunakan OpenCV
        blob_gender = cv2.dnn.blobFromImage(face_image_gender, scalefactor=1.0, size=(227, 227), mean=(78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
        gender_net.setInput(blob_gender)
        gender_preds = gender_net.forward()

        # Dapatkan indeks jenis kelamin terprediksi
        gender_idx = gender_preds[0].argmax()

        # Dapatkan jenis kelamin terprediksi
        gender = gender_list[gender_idx]

        # Tampilkan jenis kelamin pada frame
        cv2.putText(frame, f"Gender: {gender}", (left, top + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Ambil ROI untuk deteksi ekspresi wajah
        face_image_emotion = cv2.resize(frame[top:bottom, left:right], (48, 48))
        face_image_emotion = cv2.cvtColor(face_image_emotion, cv2.COLOR_BGR2GRAY)
        face_image_emotion = face_image_emotion / 255.0
        face_image_emotion = np.reshape(face_image_emotion, (1, 48, 48, 1))

        # Prediksi ekspresi wajah
        emotion_preds = emotion_model.predict(face_image_emotion)
        emotion_label = np.argmax(emotion_preds)
        emotion = emotion_labels[emotion_label]

        # Tampilkan ekspresi pada frame
        cv2.putText(frame, f"Emotion: {emotion}", (left, top + 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Tampilkan frame
    cv2.imshow('Video', frame)

    # Hentikan jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup kamera dan jendela OpenCV
cap.release()
cv2.destroyAllWindows()



