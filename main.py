import os
import time
import schedule
from web3 import Web3
from telegram import Bot
from dotenv import load_dotenv
import asyncio

# Загрузка переменных окружения
load_dotenv()
ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Загрузка переменных окружения
load_dotenv()
ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Проверка переменных окружения
if not all([ALCHEMY_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID]):
    raise ValueError("Отсутствуют переменные окружения. Проверьте .env файл.")

# Подключение к Alchemy
alchemy_url = f"https://eth-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY}"
w3 = Web3(Web3.HTTPProvider(alchemy_url))
if not w3.is_connected():
    raise Exception("Не удалось подключиться к Ethereum узлу")

# Адрес кошелька для мониторинга
USER_ADDRESS = "0x2a4cE5BaCcB98E5F95D37F8B3D1065754E0389CD"  # Замените на нужный адрес

# Адреса и ABI смарт-контрактов Compound
COMET_PROXY_ADDRESS = "0x3Afdc9BCA9213A35503b077a6072F3D0d5AB0840"
COMET_ABI = [
                    
    {
      "inputs": [],
      "name": "Absurd",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "AlreadyInitialized",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "BadAmount",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "BadAsset",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "BadDecimals",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "BadDiscount",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "BadMinimum",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "BadNonce",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "BadPrice",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "BadSignatory",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "BorrowCFTooLarge",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "BorrowTooSmall",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "InsufficientReserves",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "InvalidInt104",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "InvalidInt256",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "InvalidUInt104",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "InvalidUInt128",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "InvalidUInt64",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "InvalidValueS",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "InvalidValueV",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "LiquidateCFTooLarge",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "NegativeNumber",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "NoSelfTransfer",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "NotCollateralized",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "NotForSale",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "NotLiquidatable",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "Paused",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "ReentrantCallBlocked",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "SignatureExpired",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "SupplyCapExceeded",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "TimestampTooLarge",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "TooManyAssets",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "TooMuchSlippage",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "TransferInFailed",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "TransferOutFailed",
      "type": "error"
    },
    {
      "inputs": [],
      "name": "Unauthorized",
      "type": "error"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "absorber",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "borrower",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "collateralAbsorbed",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "usdValue",
          "type": "uint256"
        }
      ],
      "name": "AbsorbCollateral",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "absorber",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "borrower",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "basePaidOut",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "usdValue",
          "type": "uint256"
        }
      ],
      "name": "AbsorbDebt",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "Approval",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "buyer",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "baseAmount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "collateralAmount",
          "type": "uint256"
        }
      ],
      "name": "BuyCollateral",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": False,
          "internalType": "bool",
          "name": "supplyPaused",
          "type": "bool"
        },
        {
          "indexed": False,
          "internalType": "bool",
          "name": "transferPaused",
          "type": "bool"
        },
        {
          "indexed": False,
          "internalType": "bool",
          "name": "withdrawPaused",
          "type": "bool"
        },
        {
          "indexed": False,
          "internalType": "bool",
          "name": "absorbPaused",
          "type": "bool"
        },
        {
          "indexed": False,
          "internalType": "bool",
          "name": "buyPaused",
          "type": "bool"
        }
      ],
      "name": "PauseAction",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "dst",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "Supply",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "dst",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "SupplyCollateral",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "Transfer",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "TransferCollateral",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "src",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "Withdraw",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "src",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "WithdrawCollateral",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "WithdrawReserves",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "absorber",
          "type": "address"
        },
        {
          "internalType": "address[]",
          "name": "accounts",
          "type": "address[]"
        }
      ],
      "name": "absorb",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "accrueAccount",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "manager",
          "type": "address"
        },
        {
          "internalType": "bool",
          "name": "isAllowed",
          "type": "bool"
        }
      ],
      "name": "allow",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "manager",
          "type": "address"
        },
        {
          "internalType": "bool",
          "name": "isAllowed",
          "type": "bool"
        },
        {
          "internalType": "uint256",
          "name": "nonce",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "expiry",
          "type": "uint256"
        },
        {
          "internalType": "uint8",
          "name": "v",
          "type": "uint8"
        },
        {
          "internalType": "bytes32",
          "name": "r",
          "type": "bytes32"
        },
        {
          "internalType": "bytes32",
          "name": "s",
          "type": "bytes32"
        }
      ],
      "name": "allowBySig",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        }
      ],
      "name": "allowance",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "spender",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "approve",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "manager",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "approveThis",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        }
      ],
      "name": "balanceOf",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "baseAccrualScale",
      "outputs": [
        {
          "internalType": "uint64",
          "name": "",
          "type": "uint64"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "baseBorrowMin",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "baseIndexScale",
      "outputs": [
        {
          "internalType": "uint64",
          "name": "",
          "type": "uint64"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "baseMinForRewards",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "baseScale",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "baseToken",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "baseTokenPriceFeed",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "baseTrackingAccrued",
      "outputs": [
        {
          "internalType": "uint64",
          "name": "",
          "type": "uint64"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "baseTrackingBorrowSpeed",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "baseTrackingSupplySpeed",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "borrowBalanceOf",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "borrowKink",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "borrowPerSecondInterestRateBase",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "borrowPerSecondInterestRateSlopeHigh",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "borrowPerSecondInterestRateSlopeLow",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "minAmount",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "baseAmount",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "recipient",
          "type": "address"
        }
      ],
      "name": "buyCollateral",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "asset",
          "type": "address"
        }
      ],
      "name": "collateralBalanceOf",
      "outputs": [
        {
          "internalType": "uint128",
          "name": "",
          "type": "uint128"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "decimals",
      "outputs": [
        {
          "internalType": "uint8",
          "name": "",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "extensionDelegate",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "factorScale",
      "outputs": [
        {
          "internalType": "uint64",
          "name": "",
          "type": "uint64"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint8",
          "name": "i",
          "type": "uint8"
        }
      ],
      "name": "getAssetInfo",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint8",
              "name": "offset",
              "type": "uint8"
            },
            {
              "internalType": "address",
              "name": "asset",
              "type": "address"
            },
            {
              "internalType": "address",
              "name": "priceFeed",
              "type": "address"
            },
            {
              "internalType": "uint64",
              "name": "scale",
              "type": "uint64"
            },
            {
              "internalType": "uint64",
              "name": "borrowCollateralFactor",
              "type": "uint64"
            },
            {
              "internalType": "uint64",
              "name": "liquidateCollateralFactor",
              "type": "uint64"
            },
            {
              "internalType": "uint64",
              "name": "liquidationFactor",
              "type": "uint64"
            },
            {
              "internalType": "uint128",
              "name": "supplyCap",
              "type": "uint128"
            }
          ],
          "internalType": "struct CometCore.AssetInfo",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "asset",
          "type": "address"
        }
      ],
      "name": "getAssetInfoByAddress",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint8",
              "name": "offset",
              "type": "uint8"
            },
            {
              "internalType": "address",
              "name": "asset",
              "type": "address"
            },
            {
              "internalType": "address",
              "name": "priceFeed",
              "type": "address"
            },
            {
              "internalType": "uint64",
              "name": "scale",
              "type": "uint64"
            },
            {
              "internalType": "uint64",
              "name": "borrowCollateralFactor",
              "type": "uint64"
            },
            {
              "internalType": "uint64",
              "name": "liquidateCollateralFactor",
              "type": "uint64"
            },
            {
              "internalType": "uint64",
              "name": "liquidationFactor",
              "type": "uint64"
            },
            {
              "internalType": "uint128",
              "name": "supplyCap",
              "type": "uint128"
            }
          ],
          "internalType": "struct CometCore.AssetInfo",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "utilization",
          "type": "uint256"
        }
      ],
      "name": "getBorrowRate",
      "outputs": [
        {
          "internalType": "uint64",
          "name": "",
          "type": "uint64"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "asset",
          "type": "address"
        }
      ],
      "name": "getCollateralReserves",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "priceFeed",
          "type": "address"
        }
      ],
      "name": "getPrice",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getReserves",
      "outputs": [
        {
          "internalType": "int256",
          "name": "",
          "type": "int256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "utilization",
          "type": "uint256"
        }
      ],
      "name": "getSupplyRate",
      "outputs": [
        {
          "internalType": "uint64",
          "name": "",
          "type": "uint64"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getUtilization",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "governor",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "manager",
          "type": "address"
        }
      ],
      "name": "hasPermission",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "initializeStorage",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "isAbsorbPaused",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "isAllowed",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "isBorrowCollateralized",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "isBuyPaused",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "isLiquidatable",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "isSupplyPaused",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "isTransferPaused",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "isWithdrawPaused",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "liquidatorPoints",
      "outputs": [
        {
          "internalType": "uint32",
          "name": "numAbsorbs",
          "type": "uint32"
        },
        {
          "internalType": "uint64",
          "name": "numAbsorbed",
          "type": "uint64"
        },
        {
          "internalType": "uint128",
          "name": "approxSpend",
          "type": "uint128"
        },
        {
          "internalType": "uint32",
          "name": "_reserved",
          "type": "uint32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "maxAssets",
      "outputs": [
        {
          "internalType": "uint8",
          "name": "",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "name",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "numAssets",
      "outputs": [
        {
          "internalType": "uint8",
          "name": "",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bool",
          "name": "supplyPaused",
          "type": "bool"
        },
        {
          "internalType": "bool",
          "name": "transferPaused",
          "type": "bool"
        },
        {
          "internalType": "bool",
          "name": "withdrawPaused",
          "type": "bool"
        },
        {
          "internalType": "bool",
          "name": "absorbPaused",
          "type": "bool"
        },
        {
          "internalType": "bool",
          "name": "buyPaused",
          "type": "bool"
        }
      ],
      "name": "pause",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "pauseGuardian",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "priceScale",
      "outputs": [
        {
          "internalType": "uint64",
          "name": "",
          "type": "uint64"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "baseAmount",
          "type": "uint256"
        }
      ],
      "name": "quoteCollateral",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "storeFrontPriceFactor",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "supply",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "dst",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "supplyFrom",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "supplyKink",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "supplyPerSecondInterestRateBase",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "supplyPerSecondInterestRateSlopeHigh",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "supplyPerSecondInterestRateSlopeLow",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "dst",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "supplyTo",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "symbol",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "targetReserves",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "totalBorrow",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "totalSupply",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "totalsBasic",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint64",
              "name": "baseSupplyIndex",
              "type": "uint64"
            },
            {
              "internalType": "uint64",
              "name": "baseBorrowIndex",
              "type": "uint64"
            },
            {
              "internalType": "uint64",
              "name": "trackingSupplyIndex",
              "type": "uint64"
            },
            {
              "internalType": "uint64",
              "name": "trackingBorrowIndex",
              "type": "uint64"
            },
            {
              "internalType": "uint104",
              "name": "totalSupplyBase",
              "type": "uint104"
            },
            {
              "internalType": "uint104",
              "name": "totalBorrowBase",
              "type": "uint104"
            },
            {
              "internalType": "uint40",
              "name": "lastAccrualTime",
              "type": "uint40"
            },
            {
              "internalType": "uint8",
              "name": "pauseFlags",
              "type": "uint8"
            }
          ],
          "internalType": "struct CometStorage.TotalsBasic",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "totalsCollateral",
      "outputs": [
        {
          "internalType": "uint128",
          "name": "totalSupplyAsset",
          "type": "uint128"
        },
        {
          "internalType": "uint128",
          "name": "_reserved",
          "type": "uint128"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "trackingIndexScale",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "dst",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "transfer",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "dst",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "transferAsset",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "src",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "dst",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "transferAssetFrom",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "src",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "dst",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "transferFrom",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "userBasic",
      "outputs": [
        {
          "internalType": "int104",
          "name": "principal",
          "type": "int104"
        },
        {
          "internalType": "uint64",
          "name": "baseTrackingIndex",
          "type": "uint64"
        },
        {
          "internalType": "uint64",
          "name": "baseTrackingAccrued",
          "type": "uint64"
        },
        {
          "internalType": "uint16",
          "name": "assetsIn",
          "type": "uint16"
        },
        {
          "internalType": "uint8",
          "name": "_reserved",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "userCollateral",
      "outputs": [
        {
          "internalType": "uint128",
          "name": "balance",
          "type": "uint128"
        },
        {
          "internalType": "uint128",
          "name": "_reserved",
          "type": "uint128"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "name": "userNonce",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "version",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "withdraw",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "src",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "withdrawFrom",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "withdrawReserves",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "asset",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "withdrawTo",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ] # Получите ABI из https://compound.finance/docs#networks

# Инициализация контракта
contract = w3.eth.contract(address=COMET_PROXY_ADDRESS, abi=COMET_ABI)

# Настройка Telegram бота
bot = Bot(token=TELEGRAM_BOT_TOKEN)
last_hf = None
def get_health_factor():
    try:
        print("Получение данных о займах...")
        borrow_value = contract.functions.borrowBalanceOf(USER_ADDRESS).call()  # в baseToken (USDC/USDT)
        borrow_value_usdt = borrow_value / 1e6
        print(f"Общая сумма займа: {borrow_value} ({borrow_value_usdt:.2f} USDT)")

        # Используйте wstETH!
        target_assets = {
    Web3.to_checksum_address("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"): {"name": "WETH", "decimals": 18},
    Web3.to_checksum_address("0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599"): {"name": "WBTC", "decimals": 8},
    Web3.to_checksum_address("0x7f39c581f595b53c5cb19bd0b3f8da6c935e2ca0"): {"name": "wstETH", "decimals": 18},
}

        collateral_value = 0
        for asset, info in target_assets.items():
            try:
                asset_info = contract.functions.getAssetInfoByAddress(asset).call()
                price_feed = asset_info[2]
                decimals = info["decimals"]
                name = info["name"]
                collateral_factor = asset_info[4] / 1e18  # borrowCollateralFactor

                balance = contract.functions.collateralBalanceOf(USER_ADDRESS, asset).call()
                price = contract.functions.getPrice(price_feed).call()  # 1e8

                balance_token = balance / (10 ** decimals)
                price_usdt = price / 1e8
                usd_value = balance_token * price_usdt * collateral_factor

                print(f"{name}: {balance_token:.6f} x {price_usdt:.2f} x {collateral_factor:.3f} = {usd_value:.2f} USDT")
                collateral_value += usd_value
            except Exception as e:
                print(f"Ошибка по {info['name']}: {e}")

        print(f"Общая стоимость залога (с учетом collateral factor): {collateral_value:.2f} USDT")

        if collateral_value == 0:
            print("Предупреждение: Общая стоимость залога равна 0. Проверьте USER_ADDRESS и активы.")
            return float('inf') if borrow_value == 0 else 0

        hf = collateral_value / borrow_value_usdt if borrow_value_usdt > 0 else float('inf')
        print(f"Текущий Health Factor: {hf:.2f}")
        return hf
    except Exception as e:
        print(f"Ошибка при расчёте HF: {e}")
        return None


    hf_float = hf  # Не делите на 1e18!
    print(f"Текущий Health Factor: {hf_float:.2f}")

    if last_hf is None:
        last_hf_str = "N/A (первый запуск)"
    else:
        last_hf_str = f"{last_hf:.2f}"

    if last_hf is None or abs(hf_float - last_hf) >= 0.1:
        message = f"⚠️ Health Factor changed: {last_hf_str} -> {hf_float:.2f}"
        if hf_float < 1.5:
            message += "\n🚨 Warning: HF below 1.5! Consider adding collateral."
        asyncio.run(send_notification(message))
    last_hf = hf

async def send_notification(message):
    try:
        await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
        print(f"Отправлено сообщение в Telegram: {message}")
    except Exception as e:
        print(f"Ошибка отправки сообщения в Telegram: {e}")

last_hf = None  # глобальная переменная

def monitor():
    global last_hf
    hf = get_health_factor()
    if hf is None:
        return
    # Уведомлять если HF изменился на 0.2 или больше (в любую сторону)
    if last_hf is not None and abs(hf - last_hf) >= 0.2:
        direction = "снизился" if hf < last_hf else "вырос"
        message = (
            f"⚠️ Health Factor {direction}!\n"
            f"Было: {last_hf:.2f}\n"
            f"Стало: {hf:.2f}\n"
            f"Разница: {abs(hf - last_hf):.2f}\n"
        )
        asyncio.run(send_notification(message))
    last_hf = hf

# Планировщик
schedule.every(5).minutes.do(monitor)


last_hf = None

import threading
from telegram.ext import Application, CommandHandler

async def hf_command(update, context):
    hf = get_health_factor()
    if hf is not None:
        await update.message.reply_text(f"Текущий Health Factor: {hf:.2f}")
    else:
        await update.message.reply_text("Не удалось получить Health Factor.")

def run_telegram_bot():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("hf", hf_command))
    application.add_handler(CommandHandler("info", info_command)) 
    application.run_polling()

def run_scheduler():
    print("Запуск мониторинга Health Factor для Compound III...")
    monitor()  # Немедленный вызов для проверки
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except Exception as e:
            print(f"Ошибка в основном цикле: {e}")

def get_full_report():
    try:
        borrow_value = contract.functions.borrowBalanceOf(USER_ADDRESS).call()
        borrow_value_usdt = borrow_value / 1e6
        report = f"💳 <b>Общая сумма займа:</b> <code>{borrow_value_usdt:.2f} USDT</code>\n\n"

        target_assets = {
            Web3.to_checksum_address("0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"): {"name": "WETH", "decimals": 18, "emoji": "🟠"},
            Web3.to_checksum_address("0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599"): {"name": "WBTC", "decimals": 8, "emoji": "🟡"},
            Web3.to_checksum_address("0x7f39c581f595b53c5cb19bd0b3f8da6c935e2ca0"): {"name": "wstETH", "decimals": 18, "emoji": "🔵"},
        }

        collateral_value = 0
        report += "<b>Залог:</b>\n"
        for asset, info in target_assets.items():
            try:
                asset_info = contract.functions.getAssetInfoByAddress(asset).call()
                price_feed = asset_info[2]
                decimals = info["decimals"]
                name = info["name"]
                emoji = info["emoji"]
                collateral_factor = asset_info[4] / 1e18

                balance = contract.functions.collateralBalanceOf(USER_ADDRESS, asset).call()
                price = contract.functions.getPrice(price_feed).call()

                balance_token = balance / (10 ** decimals)
                price_usdt = price / 1e8
                usd_value = balance_token * price_usdt * collateral_factor

                report += (
                    f"{emoji} <b>{name}</b>: <code>{balance_token:.6f}</code> × <code>{price_usdt:.2f}</code> × "
                    f"<code>{collateral_factor:.3f}</code> = <b><code>{usd_value:.2f} USDT</code></b>\n"
                )
                collateral_value += usd_value
            except Exception as e:
                report += f"{info['name']}: ошибка получения данных ({e})\n"

        report += f"\n<b>Общая стоимость залога:</b> <code>{collateral_value:.2f} USDT</code>\n"
        hf = collateral_value / borrow_value_usdt if borrow_value_usdt > 0 else float('inf')
        report += f"\n<b>Health Factor:</b> <code>{hf:.2f}</code>"
        return report
    except Exception as e:
        return f"Ошибка при формировании отчёта: {e}"

# ...existing code...

async def info_command(update, context):
    report = get_full_report()
    await update.message.reply_text(report, parse_mode="HTML")
if __name__ == "__main__":
    # Запуск планировщика в отдельном потоке
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()
    # Запуск Telegram-бота (блокирует основной поток)
    run_telegram_bot()