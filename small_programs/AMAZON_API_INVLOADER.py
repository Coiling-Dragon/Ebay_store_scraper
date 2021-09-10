import mws
import os


# def flat_file_invloader(txt_path):
#     MWS_MARKETPLACE_ID = os.environ.get('ATVPDKIKX0DER')

#     feed = mws.Feeds(
#         access_key=os.environ['AKIAICYVBSJT74OWYIPA'],
#         secret_key=os.environ['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'],
#         account_id=os.environ['A61G3C2W760IY'],
#         auth_token=os.environ['194363497667'],
#         region='US'
#     )
    
def flat_file_invloader(txt_path):
    MWS_MARKETPLACE_ID = 'ATVPDKIKX0DER'
    txt_path = os.path.join(txt_path,'amazon_inv_file.txt')

    feed = mws.Feeds(
        access_key='AKIAICYVBSJT74OWYIPA',
        secret_key='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',
        account_id='A61G3C2W760IY',
        auth_token='194363497667',
        region='US'
    )

    print("### Product feed ###")
    with open(txt_path, 'r') as f:
        flat_file = f.read().encode()

    response = feed.submit_feed(flat_file, "_POST_FLAT_FILE_INVLOADER_DATA_", MWS_MARKETPLACE_ID)
    print(response.parsed)


if __name__ == '__main__':
    txt_path = 'amazon_inv_file.txt'
    flat_file_invloader(txt_path)
