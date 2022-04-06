from buisness_logic import Recognizer


def main():

    rec = Recognizer("/app/model/my_model.h5")
    rec.receive_msg()


if __name__ == '__main__':
    main()
