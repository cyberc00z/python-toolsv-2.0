import io
import zipfile


def compress_file(output_file, path):
    compression = zipfile.ZIP_DEFLATED
    zf = zipfile.ZipFile(output_file, mode='w')

    try:
           
        zf.write(path, output_file, compress_type=compression)

    except Exception as error:
        print(error)

def main():
    print("Enter number of files you want to compress: ")
    inp = int(input())
    no_file_paths = inp
    for path in range(no_file_paths):
        path = input(str("Enter Path Name of %s'th file : " %(path)))
        print(path)

    output_file = "./res/output.zip"
    #call compression function
    compress_file(output_file, path)

    
if __name__ == '__main__':
    main()



